/* DSPIRA lessons — site behaviour. Vanilla ES5, no dependencies.

   There is no menu code here. The masthead's mobile menu is the WVU Design
   System's own: its navigation script (loaded by the layout, after <main>)
   looks for .js-wvu-site-nav-toggle and .js-wvu-site-nav-items, toggles
   is-opened and aria-expanded, swaps "Open Menu" / "Close Menu", and closes
   on Escape. This script retires the old service worker, filters lessons,
   and makes overflowing content keyboard-accessible.                                                */
(function () {
   "use strict";

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

   // Filter lessons and hide modules without matches.
   var filterBox = document.querySelector("[data-lesson-filter]");
   if (filterBox) {
      var input = filterBox.querySelector("#lesson-filter");
      var count = filterBox.querySelector(".filter__count");
      var jump = filterBox.querySelector("[data-results-link]");
      var clear = filterBox.querySelector("[data-clear-filter]");
      var cards = [].slice.call(document.querySelectorAll(".lesson-card[data-search]"));
      var groups = [].slice.call(document.querySelectorAll("[data-module]"));
      var intros = [].slice.call(document.querySelectorAll("[data-module-intro]"));
      filterBox.hidden = false;

      var normalize = function (text) {
         return text.toLowerCase()
            .replace(/calibrat(?:ions?|ing|ed|e)?/g, "calibrat")
            .replace(/install(?:ations?|ing|ed)?/g, "install")
            .replace(/observ(?:ations?|ing|ed|e)/g, "observ")
            .replace(/[^a-z0-9]+/g, " ").trim();
      };
      var apply = function () {
         var q = input.value.trim();
         var terms = normalize(q).split(/\s+/).filter(Boolean);
         var shown = 0;
         cards.forEach(function (card) {
            var words = normalize(card.getAttribute("data-search"));
            var hit = terms.every(function (term) { return words.indexOf(term) !== -1; });
            card.hidden = !hit;
            if (hit) shown++;
         });
         groups.forEach(function (group) {
            group.hidden = !group.querySelector(".lesson-card:not([hidden])");
         });
         intros.forEach(function (intro) { intro.hidden = !!q; });
         jump.hidden = !q || !shown;
         clear.hidden = !q;
         count.textContent = !q ? "" : shown === 0
            ? "No lessons match. Try another search or clear the filter."
            : shown + " of " + cards.length + " lessons match";
      };
      var update = function () {
         var url = new URL(window.location.href);
         if (input.value.trim()) url.searchParams.set("q", input.value.trim());
         else url.searchParams.delete("q");
         window.history.replaceState(window.history.state, "", url.toString());
         apply();
      };
      var restore = function () {
         input.value = new URL(window.location.href).searchParams.get("q") || "";
         apply();
      };
      input.addEventListener("input", update);
      window.addEventListener("pageshow", restore);
      window.addEventListener("popstate", restore);
      input.addEventListener("keydown", function (event) {
         if (event.key === "Escape") { input.value = ""; update(); }
      });
      clear.addEventListener("click", function () {
         input.value = "";
         update();
         input.focus();
      });
      restore();
   }

   /* --- Scrollable code blocks and tables --------------------------------
      A lesson's code samples are wider than the column on a narrow screen, so
      the stylesheet lets them scroll sideways. A region you can only scroll
      with a mouse or a finger is unreachable from the keyboard, which is
      WCAG 2.1.1; giving it a tab stop and a name fixes that. Only blocks that
      actually overflow get one, so the tab order does not fill up with code
      samples that fit. Re-measured on resize because the column narrows. */
   var scrollables = function () {
      var blocks = document.querySelectorAll("pre, .highlight, .highlighter-rouge");
      for (var i = 0; i < blocks.length; i++) {
         var el = blocks[i];
         if (el.querySelector("pre, .highlight")) { continue; }  /* only the innermost */
         var overflows = el.scrollWidth > el.clientWidth + 1;
         if (overflows && !el.hasAttribute("tabindex")) {
            el.setAttribute("tabindex", "0");
            el.setAttribute("role", "region");
            el.setAttribute("aria-label", "Code sample " + (i + 1) + ", scrollable");
         } else if (!overflows && el.getAttribute("role") === "region") {
            el.removeAttribute("tabindex");
            el.removeAttribute("role");
            el.removeAttribute("aria-label");
         }
      }
      // Keep native table semantics while allowing keyboard scrolling.
      var tables = document.querySelectorAll(".prose table");
      for (var j = 0; j < tables.length; j++) {
         var table = tables[j];
         if (table.scrollWidth > table.clientWidth + 1 && !table.hasAttribute("tabindex")) {
            table.setAttribute("tabindex", "0");
            table.setAttribute("data-scroll-focus", "true");
         } else if (table.scrollWidth <= table.clientWidth + 1 && table.hasAttribute("data-scroll-focus")) {
            table.removeAttribute("tabindex");
            table.removeAttribute("data-scroll-focus");
         }
      }
   };
   scrollables();
   var resizeTimer;
   window.addEventListener("resize", function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(scrollables, 200);
   });

})();
