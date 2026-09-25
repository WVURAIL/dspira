const assert = require('node:assert/strict');
const { test } = require('node:test');
const { readFileSync } = require('node:fs');
const { join } = require('node:path');
const vm = require('node:vm');

function fixture(query = '') {
  const element = () => ({ hidden: false, value: '', textContent: '', events: {},
    addEventListener(type, fn) { this.events[type] = fn; }, focus() {} });
  const input = element(), count = element(), jump = element(), clear = element();
  const controls = { '#lesson-filter': input, '.filter__count': count,
    '[data-results-link]': jump, '[data-clear-filter]': clear };
  const filter = { hidden: true, querySelector: selector => controls[selector] };
  const cards = ['How to Calibrate the Horn Telescope Observing',
    'Installing GNU Radio Software Setup', 'Fourier Analysis Digital Signal Processing']
    .map(text => ({ hidden: false, getAttribute: () => text }));
  const groups = cards.map(card => ({ hidden: false, querySelector: () => card.hidden ? null : card }));
  const intros = cards.map(element);
  const win = { location: { href: 'https://example.test/dspira/all/' + query }, events: {},
    addEventListener(type, fn) { this.events[type] = fn; } };
  win.history = { state: null, replaceState(state, title, url) { win.location.href = url; } };
  const document = {
    querySelector: selector => selector === '[data-lesson-filter]' ? filter : null,
    querySelectorAll: selector => ({ '.lesson-card[data-search]': cards,
      '[data-module]': groups, '[data-module-intro]': intros }[selector] || [])
  };
  vm.runInNewContext(readFileSync(join(__dirname, '../assets/js/lessons.js'), 'utf8'),
    { window: win, document, navigator: {}, URL, setTimeout, clearTimeout });
  return { input, count, jump, clear, cards, groups, intros, win };
}

test('a natural calibration query finds its differently inflected title', () => {
  const f = fixture(); f.input.value = 'CALIBRATION'; f.input.events.input();
  assert.deepEqual(f.cards.map(c => c.hidden), [false, true, true]);
  assert.deepEqual(f.groups.map(c => c.hidden), [false, true, true]);
  assert.equal(f.count.textContent, '1 of 3 lessons match');
  assert.equal(f.jump.hidden, false);
  assert.ok(f.intros.every(i => i.hidden));
});

test('word variants and multiple terms work without depending on word order', () => {
  const f = fixture(); f.input.value = 'radio installation'; f.input.events.input();
  assert.deepEqual(f.cards.map(c => c.hidden), [true, false, true]);
});

test('a shared URL restores the query and results', () => {
  const f = fixture('?q=calibration');
  assert.equal(f.input.value, 'calibration');
  assert.equal(f.cards[0].hidden, false);
  assert.equal(f.cards[1].hidden, true);
});

test('Back and page restoration use the saved URL', () => {
  const f = fixture(); f.input.value = 'Fourier'; f.input.events.input();
  assert.equal(new URL(f.win.location.href).searchParams.get('q'), 'Fourier');
  f.input.value = ''; f.win.events.pageshow();
  assert.equal(f.input.value, 'Fourier');
  assert.deepEqual(f.cards.map(c => c.hidden), [true, true, false]);
});

test('no-match queries offer recovery and clear preserves other URL parameters', () => {
  const f = fixture('?from=class#lesson-results');
  f.input.value = 'not-a-real-topic'; f.input.events.input();
  assert.ok(f.cards.every(c => c.hidden));
  assert.equal(f.jump.hidden, true);
  assert.equal(f.clear.hidden, false);
  assert.match(f.count.textContent, /No lessons match/);
  f.clear.events.click();
  assert.ok(f.cards.every(c => !c.hidden));
  assert.equal(f.win.location.href, 'https://example.test/dspira/all/?from=class#lesson-results');
  assert.equal(f.count.textContent, '');
});

test('Escape clears both the field and its saved query', () => {
  const f = fixture('?q=calibration'); f.input.events.keydown({key:'Escape'});
  assert.equal(f.input.value, '');
  assert.equal(new URL(f.win.location.href).searchParams.has('q'), false);
});

test('plural and past-tense calibration variants resolve to the same lesson', () => {
  for (const word of ['calibrate', 'calibrated', 'calibrating', 'calibration', 'calibrations']) {
    const f = fixture(); f.input.value = word; f.input.events.input();
    assert.equal(f.cards[0].hidden, false, word);
    assert.equal(f.cards[1].hidden, true, word);
  }
});
