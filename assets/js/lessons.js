/* DSPIRA lessons — site behaviour. Vanilla, no dependencies. */
(function () {
   "use strict";

   /* --- Mobile navigation ------------------------------------------------ */
   var toggle = document.querySelector(".nav-toggle");
   if (toggle) {
      var setOpen = function (open) {
         document.documentElement.toggleAttribute("data-nav-open", open);
         toggle.setAttribute("aria-expanded", String(open));
      };
      toggle.addEventListener("click", function () {
         setOpen(!document.documentElement.hasAttribute("data-nav-open"));
      });
      document.addEventListener("keydown", function (e) {
         if (e.key === "Escape") setOpen(false);
      });
      document.querySelectorAll(".site-nav a").forEach(function (a) {
         a.addEventListener("click", function () { setOpen(false); });
      });
   }

   /* --- Video embeds ------------------------------------------------------
      Lessons are written by teachers in plain Markdown, and the authoring
      convention is to paste a YouTube URL on a line by itself. This turns
      those into responsive embeds.

      It runs on the rendered paragraph rather than at build time because
      GitHub Pages only permits its own plugin allowlist. If this script does
      not run, the URL stays a visible, clickable link — which is why the URL
      is left in place as the fallback rather than being replaced.        */
   var YT = /^https?:\/\/(?:www\.)?(?:youtube\.com\/(?:watch\?v=|embed\/)|youtu\.be\/)([\w-]{11})/;

   document.querySelectorAll(".prose p").forEach(function (p) {
      var text = p.textContent.trim();
      var link = p.querySelector("a");
      // Only a paragraph that is nothing but the URL.
      if (p.children.length > 1) return;
      if (link && link.textContent.trim() !== text) return;

      var m = YT.exec(text);
      if (!m) return;

      var wrap = document.createElement("div");
      wrap.className = "videoWrapper";
      var frame = document.createElement("iframe");
      frame.src = "https://www.youtube-nocookie.com/embed/" + m[1];
      frame.title = "Video";
      frame.loading = "lazy";
      frame.allow = "accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
      frame.allowFullscreen = true;
      wrap.appendChild(frame);
      p.replaceWith(wrap);
   });

   /* --- Retire the old service worker ------------------------------------
      The previous theme registered a cache-first service worker with no
      skipWaiting(). It cached the stylesheet and the index page and kept
      serving them, so a returning visitor could see the old site for as long
      as they kept a tab open. Deleting sw.js is not enough on its own —
      browsers that already installed it need to be told to let go.       */
   if ("serviceWorker" in navigator) {
      navigator.serviceWorker.getRegistrations().then(function (regs) {
         regs.forEach(function (r) { r.unregister(); });
      }).catch(function () { /* nothing to clean up */ });
      if (window.caches && caches.keys) {
         caches.keys().then(function (names) {
            names.forEach(function (n) { caches.delete(n); });
         }).catch(function () { /* nothing to clean up */ });
      }
   }

   /* --- Filter on /all/ ---------------------------------------------------
      The page used to tell the reader to press Ctrl-F. Forty-eight cards is
      past the point where that is a reasonable answer, and it is no answer at
      all on a phone, where there is no Ctrl-F to press.

      Progressive enhancement: the box is `hidden` in the markup and revealed
      here, so with JavaScript off the reader gets the full list, which is what
      the page did before. Matching is against a `data-search` attribute built
      at render time from title, summary and module name -- cheaper than walking
      the DOM for text on every keystroke, and it lets a search for "raspberry"
      find a lesson whose title never says it.                              */
   var filterBox = document.querySelector("[data-lesson-filter]");
   if (filterBox) {
      var input = filterBox.querySelector(".filter__input");
      var count = filterBox.querySelector(".filter__count");
      var cards = [].slice.call(document.querySelectorAll(".lesson-card[data-search]"));
      var groups = [].slice.call(document.querySelectorAll("[data-module]"));
      var total = cards.length;

      filterBox.hidden = false;

      var apply = function () {
         var q = input.value.trim().toLowerCase();
         var shown = 0;

         cards.forEach(function (card) {
            var hit = q === "" || card.getAttribute("data-search").indexOf(q) !== -1;
            card.hidden = !hit;
            if (hit) shown++;
         });

         /* A module whose lessons all dropped out says so rather than
            collapsing to a bare heading with nothing under it. */
         groups.forEach(function (g) {
            var any = g.querySelector(".lesson-card:not([hidden])") !== null;
            var note = g.querySelector(".no-matches");
            if (note) note.hidden = any;
            g.classList.toggle("is-empty", !any);
         });

         if (q === "") {
            count.textContent = "";
         } else {
            count.textContent = shown === 0
               ? "No lessons match \u201c" + input.value.trim() + "\u201d"
               : shown + " of " + total + " lessons match";
         }
      };

      input.addEventListener("input", apply);
      input.addEventListener("keydown", function (e) {
         if (e.key === "Escape") { input.value = ""; apply(); }
      });
      apply();
   }

})();
