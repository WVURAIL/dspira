# Contributing

Lessons are Markdown files in `_posts/`. The quickest route is to open a pull
request; the walkthrough with screenshots is at
<https://wvurail.org/dspira/newpost/>.

1. Name the file `YYYY-MM-DD-Short-Name.md`.
2. Give it front matter — `title`, `summary`, `categories`, `order`, `tags`.
   `categories` must hold exactly one name, matching a `category:` in
   `_data/modules.yml`; `order` is the lesson's place in that module, counting
   from 1. The build checks both.
3. Start headings at `##`. The layout supplies the `h1`, and every page gets
   exactly one.
4. Put images in `images/` and reference them as
   `![what the picture shows]({{ site.baseurl }}/images/your-file.png)`. The
   alt text is not optional.
5. A link becomes a button with `{: .btn .btn-wvu-blue}` after it, or
   `{: .btn .btn-wvu-gold}` for the one primary action on a page. Not the old
   `{: .button}`.
6. Open the pull request. The build check has to pass before it can merge; if it
   goes red, the log says which page broke.

Questions: <rail@wvu.edu>, or a thread in
[GitHub Discussions](https://github.com/WVURAIL/dspira/discussions),
which is where the site's forum pages point.
