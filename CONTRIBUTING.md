# Contributing

Lessons are Markdown files in `_posts/`. The quickest route is to open a pull
request; the walkthrough with screenshots is at
<https://wvurail.org/dspira-lessons/newpost/>.

1. Name the file `YYYY-MM-DD-Short-Name.md`.
2. Give it front matter — `title`, `summary`, `categories`, `order`, `tags`.
   `categories` must hold exactly one name, matching a `category:` in
   `_data/modules.yml`; `order` is the lesson's place in that module, counting
   from 1. The build checks both.
3. Put images in `images/` and reference them as
   `{{ site.baseurl }}/images/your-file.png`.
4. Open the pull request. The build check has to pass before it can merge; if it
   goes red, the log says which page broke.

Questions: <wvurail@gmail.com>.
