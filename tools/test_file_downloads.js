const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

const code = fs.readFileSync(path.join(__dirname, '../assets/js/file-downloads.js'), 'utf8');
const source = 'https://raw.githubusercontent.com/WVURAIL/dspira-software/main/examples/filters/fundamental-frequency-fir.grc';

function setup(fetch, href = source) {
   const downloads = [], blobs = [], statuses = [], timers = [];
   function element() {
      return {
         children: [], attributes: {},
         setAttribute(key, value) { this.attributes[key] = value; },
         removeAttribute(key) { delete this.attributes[key]; },
         appendChild(child) { this.children.push(child); },
         after(child) { statuses.push(child); },
         addEventListener(name, callback) { this[name] = callback; },
         click() { downloads.push({ href: this.href, filename: this.download }); },
         remove() {},
      };
   }
   const link = element();
   link.href = href;
   class DownloadURL extends URL {}
   DownloadURL.createObjectURL = blob => { blobs.push(blob); return 'blob:download'; };
   DownloadURL.revokeObjectURL = () => {};
   vm.runInNewContext(code, {
      window: { fetch, AbortController }, fetch, AbortController, URL: DownloadURL, Blob,
      document: {
         querySelectorAll: () => [link], createElement: element,
         createTextNode: text => ({ textContent: text }), body: element(),
      },
      setTimeout: (callback, delay) => { timers.push({ callback, delay }); return timers.length; },
      clearTimeout() {},
   });
   function click(overrides = {}) {
      const event = { button: 0, prevented: false, preventDefault() { this.prevented = true; }, ...overrides };
      return { event, done: link.click(event) };
   }
   return { link, click, downloads, blobs, statuses, timers };
}

test('downloads the original bytes with the GRC filename', async () => {
   const calls = [];
   const env = setup(async (...args) => {
      calls.push(args);
      return { ok: true, blob: async () => new Blob(['<flow_graph>example</flow_graph>']) };
   });
   const { event, done } = env.click();
   await done;
   assert.equal(event.prevented, true);
   assert.equal(calls[0][0], source);
   assert.equal(calls[0][1].credentials, 'omit');
   assert.equal(env.downloads[0].filename, 'fundamental-frequency-fir.grc');
   assert.equal(env.blobs[0].type, 'application/octet-stream');
   assert.equal(await env.blobs[0].text(), '<flow_graph>example</flow_graph>');
   assert.match(env.statuses[0].textContent, /Download started/);
   assert.equal(env.link.attributes['aria-busy'], undefined);
});

test('HTTP errors do not download error pages and offer a source link', async () => {
   const env = setup(async () => ({ ok: false }));
   await env.click().done;
   assert.equal(env.downloads.length, 0);
   assert.match(env.statuses[0].textContent, /Download failed/);
   assert.equal(env.statuses[0].children[0].href, source);
   assert.equal(env.link.attributes['aria-busy'], undefined);
});

test('network failures allow another attempt', async () => {
   let count = 0;
   const env = setup(async () => {
      if (++count === 1) throw new Error('Offline');
      return { ok: true, blob: async () => new Blob(['flowgraph']) };
   });
   await env.click().done;
   await env.click().done;
   assert.equal(count, 2);
   assert.equal(env.downloads.length, 1);
});

test('repeated clicks do not start concurrent downloads', async () => {
   let finish, calls = 0;
   const env = setup(() => { calls++; return new Promise(resolve => { finish = resolve; }); });
   const first = env.click();
   await env.click().done;
   assert.equal(calls, 1);
   finish({ ok: true, blob: async () => new Blob(['flowgraph']) });
   await first.done;
   assert.equal(env.downloads.length, 1);
});

test('modified clicks keep normal browser navigation', async () => {
   const env = setup(() => { throw new Error('Should not fetch'); });
   for (const modifiers of [{ ctrlKey: true }, { metaKey: true }, { shiftKey: true }, { altKey: true }, { button: 1 }]) {
      const { event, done } = env.click(modifiers);
      await done;
      assert.equal(event.prevented, false);
   }
   assert.equal(env.downloads.length, 0);
});

test('only the approved raw GRC sources get a download handler', () => {
   for (const href of ['https://example.com/example.grc', source.replace('.grc', '.pdf'), source.replace('WVURAIL', 'another-user')]) {
      const env = setup(() => { throw new Error('Should not fetch'); }, href);
      assert.equal(env.link.click.name, 'click');
      assert.equal(env.statuses.length, 0);
   }
});

test('stalled downloads are canceled', async () => {
   const env = setup((url, options) => new Promise((resolve, reject) => {
      options.signal.addEventListener('abort', () => reject(new Error('Aborted')));
   }));
   const attempt = env.click();
   const timeout = env.timers.find(timer => timer.delay === 20000);
   timeout.callback();
   await attempt.done;
   assert.equal(env.downloads.length, 0);
   assert.match(env.statuses[0].textContent, /Download failed/);
});
