/* DSPIRA lessons — the "New Post" page. Vanilla ES5, no dependencies.

   This was an inline <script> at the foot of pages/newpost.md until the move
   to the University domain. Inline script is the first thing a content
   security policy blocks, and this was the last of it on the site outside the
   two exported notebooks, so it lives in a file now. The behaviour is
   unchanged: stamp today's date into the page, and hand back the textarea as
   a .md file named the way _posts wants it.

   Loaded by that one page, but guarded so that loading it anywhere else does
   nothing.                                                                */
(function () {
   "use strict";

   var stamp = document.getElementById("date");
   var button = document.getElementById("save-post");
   var textarea = document.getElementById("inputTextToSave");
   var nameBox = document.getElementById("inputFileNameToSaveAs");

   // Not the New Post page.
   if (!stamp && !button) return;

   /* --- Today, in the form _posts names its files -------------------------
      Jekyll reads a post's date off its filename, so the date shown on the
      page is the one prefixed to the download. Worked out once, at load, as
      the inline version did — a page left open past midnight keeps the date
      it was opened with.                                                  */
   var n = new Date();
   var y = n.getFullYear();
   var m = n.getMonth() + 1;
   var d = n.getDate();

   if (d < 10) { d = "0" + d; }
   if (m < 10) { m = "0" + m; }

   var datetoday = y + "-" + m + "-" + d;

   if (stamp) { stamp.textContent = datetoday; }

   /* --- Save the textarea as a file --------------------------------------
      The site is static, so there is nothing to POST to: the text becomes a
      Blob and the browser downloads it from an object URL. The anchor that
      carries the download is created hidden, clicked, and removes itself
      again, so nothing of it is ever visible.                            */
   function destroyClickedElement(event) {
      document.body.removeChild(event.target);
   }

   function saveTextAsFile() {
      if (!textarea || !nameBox) return;

      var textToSave = textarea.value;
      var textToSaveAsBlob = new Blob([textToSave], { type: "text/plain" });
      var textToSaveAsURL = window.URL.createObjectURL(textToSaveAsBlob);
      var fileNameToSaveAs = datetoday + "-" + nameBox.value + ".md";

      var downloadLink = document.createElement("a");
      downloadLink.download = fileNameToSaveAs;
      downloadLink.textContent = "Download File";
      downloadLink.href = textToSaveAsURL;
      downloadLink.onclick = destroyClickedElement;
      downloadLink.style.display = "none";
      document.body.appendChild(downloadLink);

      downloadLink.click();
   }

   if (button) {
      button.addEventListener("click", saveTextAsFile);
   }

})();
