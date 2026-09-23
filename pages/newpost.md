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
Add an embedded window of the youtube video to the page by simply pasting the YouTube link on the markdown page on its own. Please add a couple of lines describing the contents of the video at minimum. 

```
https://www.youtube.com/watch?v=jS5fTzMP_mg

The above video is a video of Kermit the frog singing the Rainbow Connection
```
### Adding images to the posts

To add images to your post first upload your image to github by going to the link below  upload and commit an image to the images directory: 

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
 
