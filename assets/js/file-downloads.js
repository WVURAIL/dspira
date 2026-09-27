/* Save flowgraphs without navigating away from the lesson. */
(function () {
   "use strict";
   if (!window.fetch || !window.AbortController || !URL.createObjectURL) return;

   document.querySelectorAll("a[data-download]").forEach(function (link) {
      var source = new URL(link.href);
      if (source.origin !== "https://raw.githubusercontent.com" ||
          !/^\/WVURAIL\/(dspira-software|radio-research-software)\/main\/.+\.grc$/.test(source.pathname)) return;
      var filename = decodeURIComponent(source.pathname.split("/").pop());
      var pending = false;
      var status;

      link.addEventListener("click", async function (event) {
         if (event.defaultPrevented || event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
         event.preventDefault();
         if (pending) return;
         pending = true;
         link.setAttribute("aria-busy", "true");
         if (!status) {
            status = document.createElement("span");
            status.setAttribute("role", "status");
            link.after(status);
         }
         status.textContent = " Preparing download…";
         var controller = new AbortController();
         var timer = setTimeout(function () { controller.abort(); }, 20000);
         try {
            // GitHub serves GRC files as text and ignores cross-origin download attributes.
            var response = await fetch(source.href, { credentials: "omit", signal: controller.signal });
            if (!response.ok) throw new Error("Download failed");
            var blob = new Blob([await response.blob()], { type: "application/octet-stream" });
            var address = URL.createObjectURL(blob);
            var save = document.createElement("a");
            save.href = address;
            save.download = filename;
            save.hidden = true;
            document.body.appendChild(save);
            save.click();
            save.remove();
            setTimeout(function () { URL.revokeObjectURL(address); }, 60000);
            status.textContent = " Download started.";
         } catch (error) {
            status.textContent = " Download failed. Try again, or ";
            var fallback = document.createElement("a");
            fallback.href = source.href;
            fallback.textContent = "open the source file";
            status.appendChild(fallback);
            status.appendChild(document.createTextNode(" and choose Save Page As to save the GRC file."));
         } finally {
            clearTimeout(timer);
            pending = false;
            link.removeAttribute("aria-busy");
         }
      });
   });
})();
