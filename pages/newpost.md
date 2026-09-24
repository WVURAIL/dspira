---
layout: page
title: New Post
permalink: /newpost/
meta_description: "Write a new DSPIRA lesson in Markdown. Use the formatting guide and browser editor to prepare headings, images, links, and lesson metadata."
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

- Quote titles and summaries containing special characters such as `:`. For example: `title: "my awesome site: an adventure".`
- Every *post* can have one `tag` or multiple `tags`. It will automatically split a string entry if it contains whitespace. Jekyll expects multiple entries under tags. The front matter `tag: classic hollywood` creates one entry, `"classic hollywood"`. By contrast, `tags: classic hollywood` creates the array `["classic", "hollywood"]`. 
- `categories` does **not** work the way `tags` does. Each lesson belongs to one module. Its name must match a `category:` entry in `_data/modules.yml` exactly. Options include *Horn Construction*, *Receiver Electronics*, and *Software Setup*. Other options are *Observing*, *Digital Signal Processing*, *Astronomy*, and *Community Labs*. A name that matches nothing means the lesson appears in no
module at all, and the build will say so.

- `order` is where the lesson sits inside its module, counting from 1. Every
index and the previous/next links sort by it. Take the next free number in the
module, or renumber the others if your lesson belongs partway through.

- Write your lesson after the front matter using `markdown`. Consult the [Markdown cheat sheet](https://github.com/WVURAIL/dspira-lessons/wiki/Markdown-Cheatsheet)

- Add buttons to link to a pdf of your document using this syntax

```
[Google](http://www.google.com){: .btn .btn-wvu-blue}
```

In Google Drive:
- open document
- click share button (upper right corner)
- in dialog box, change the get link attribute to Anyone with link with viewer privileges. see screenshot below

![screen shot of changing permissions of google document]({{ site.baseurl }}/images/SharedScreenshot.jpg)

EXAMPLE:
- To add a Google doc lesson:
```
[Name of your lesson](https://link/to/your/document/dotcom){: .btn .btn-wvu-blue}
```

- Add YouTube link:

Paste a YouTube link on its own line in the Markdown page. This creates an embedded video window. Please add a couple of lines describing the contents of the video at minimum. 

```
https://www.youtube.com/watch?v=jS5fTzMP_mg

The above video is a video of Kermit the frog singing the Rainbow Connection
```
### Adding images to the posts

To add an image, upload it to GitHub's images directory using the link below. Commit the uploaded file: 

[Upload image](https://github.com/WVURAIL/dspira-lessons/upload/master/images){: .btn .btn-wvu-blue}

Then add the following to the post you are editing
```
![write-a-brief-alt-text-describing-your-image]({{ site.baseurl }}/images/name-of-your-image-file.FORMAT)
```
### View the live webpage: [the live lessons site]({{ site.baseurl }}/)


##  Edit your post in the text area below 

<div>
    <p>Date: <span id="date"></span></p>
    <div>
    <label for="inputTextToSave" class="form-label helvetica-neue-bold">Your lesson, in Markdown</label>
    <textarea id="inputTextToSave" class="form-control" cols="80" rows="25">
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
    <label for="inputFileNameToSaveAs" class="form-label helvetica-neue-bold">Filename to save as</label>
    <div class="d-flex align-items-center gap-2 flex-wrap">
      <input id="inputFileNameToSaveAs" class="form-control w-auto" type="text">
      <span aria-hidden="true">.md</span>
      <button type="button" id="save-post" class="btn btn-wvu-blue">Save</button>
    </div>
    </div>
</div>

<div> Upload your saved file to the website by uploading and committing on github.com: &nbsp;
 <a href="https://github.com/WVURAIL/dspira-lessons/upload/master/_posts" class="btn btn-wvu-blue">Upload to Website</a>
</div>

<script src="{{ '/assets/js/newpost.js' | relative_url }}" defer></script>
 
