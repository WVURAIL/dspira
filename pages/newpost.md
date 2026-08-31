---
layout: page
title: New Post
permalink: /newpost/
---

These are instructions and a simple template to start creating a new post!

## Syntax hints for post formatting

All post files must begin with *front matter* which is typically used to set a layout or other meta data. For a simple example this can just be empty:


```
---
layout:     post
date:       2020-07-09 21:21:29
title:      Title of your Lesson
summary:    Summary of your Lesson
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Observing']
order:      11
---
```

- Make sure you do not have special characters like `:` in your title and/or summary quote any special characters, such as `:` like `title: "my awesome site: an adventure".`
- Every *post* can have one `tag` or multiple `tags`. It will automatically split a string entry if it contains whitespace. The website software, Jekyll, expects multiple items mapped to the key tags For example, while front matter `tag: classic hollywood` will be processed into a singular entity `"classic hollywood"`, front matter `tags: classic hollywood` will be processed into an array of entries `["classic", "hollywood"]`. 
- `categories` does **not** work the way `tags` does. A lesson belongs to
exactly one module, and the name has to match one of the `category:` entries in
`_data/modules.yml` exactly — *Horn Construction*, *Receiver Electronics*,
*Software Setup*, *Observing*, *Digital Signal Processing*, *Astronomy* or
*Community Labs*. A name that matches nothing means the lesson appears in no
module at all, and the build will say so.

- `order` is where the lesson sits inside its module, counting from 1. Every
index and the previous/next links sort by it. Take the next free number in the
module, or renumber the others if your lesson belongs partway through.

- After the front matter make your lesson post formatting it in `markdown` refer to this cheat sheet [https://github.com/WVURAIL/dspira-lessons/wiki/Markdown-Cheatsheet](https://github.com/WVURAIL/dspira-lessons/wiki/Markdown-Cheatsheet)

- Add buttons to link to a pdf of your document using this syntax

```
[Google](http://www.google.com){: .button}
```

In Google Drive:
- open document
- click share button (upper right corner)
- in dialog box, change the get link attribute to Anyone with link with viewer privileges. see screenshot below

![screen shot of changing permissions of google document]({{ site.baseurl }}/images/SharedScreenshot.jpg)

EXAMPLE:
- To add a Google doc lesson:
```
[Name of your lesson](https://link/to/your/document/dotcom){: .button}
```

- Add YouTube link:
Add an embedded window of the youtube video to the page by simply pasting the YouTube link on the markdown page on its own. Please add a couple of lines describing the contents of the video at minimum. 

```
https://www.youtube.com/watch?v=jS5fTzMP_mg

The above video is a video of Kermit the frog singing the Rainbow Connection
```
##### Adding images to the posts

To add images to your post first upload your image to github by going to the link below  upload and commit an image to the images directory: 

[Upload image](https://github.com/WVURAIL/dspira-lessons/upload/master/images){: .button}

Then add the following to the post you are editing
```
![write-a-brief-alt-text-describing-your-image]({{ site.baseurl }}/images/name-of-your-image-file.FORMAT)
```
### View the live webpage: [the live lessons site]({{ site.baseurl }}/)


##  Edit your post in the text area below 

<div>
    <p>Date:</p><h2 id="date"></h2>
    <div>
    <textarea id="inputTextToSave" cols="80" rows="25">
---
layout: post
date:   copy date from above
title: edit this title
summary:  edit this a ~10 word summary
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['category', 'Subcategory'] 
---

Enter the Lesson posts here
    </textarea></div>
    <div>
    Filename to Save As: &nbsp; <input id="inputFileNameToSaveAs">&nbsp;.md
    <button onclick="saveTextAsFile()">Save</button>
    </div>
</div>

<div> Upload your saved file to the website by uploading and committing on github.com: &nbsp;
 <a href="https://github.com/WVURAIL/dspira-lessons/upload/master/_posts" class = "button">Upload to Website</a>
</div>

<script type="text/javascript">
 
n =  new Date();
y = n.getFullYear();
m = n.getMonth() + 1;
d = n.getDate();

if (d < 10) {
  d = '0' + d;
}
if (m < 10) {
  m = '0' + m;
}

datetoday = y + "-" + m + "-" + d;
document.getElementById("date").innerHTML = datetoday

function saveTextAsFile()
{
    var textToSave = document.getElementById("inputTextToSave").value;
    var textToSaveAsBlob = new Blob([textToSave], {type:"text/plain"});
    var textToSaveAsURL = window.URL.createObjectURL(textToSaveAsBlob);
    var fileNameToSaveAs = datetoday + "-" + document.getElementById("inputFileNameToSaveAs").value + ".md";
 
    var downloadLink = document.createElement("a");
    downloadLink.download = fileNameToSaveAs;
    downloadLink.innerHTML = "Download File";
    downloadLink.href = textToSaveAsURL;
    downloadLink.onclick = destroyClickedElement;
    downloadLink.style.display = "none";
    document.body.appendChild(downloadLink);
 
    downloadLink.click();
}
 
function destroyClickedElement(event)
{
    document.body.removeChild(event.target);
}

</script>
 
