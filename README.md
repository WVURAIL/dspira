# DSPIRA lessons

The lesson site for **Digital Signal Processing in Radio Astronomy** — free
material on building and using a horn radio telescope, written by the high
school teachers who did it.

Live at <https://wvurail.org/dspira-lessons/>. Built by GitHub Pages from the
`master` branch.

## How it is put together

| Path | What it is |
|---|---|
| `_posts/` | The lessons - 48 at last count. One Markdown file each. |
| `_data/modules.yml` | The module order and blurbs. Drives the front page and `/all/`. |
| `_data/nav.yml` | Site navigation. Edit here, every page follows. |
| `categories/*/index.md` | One page per module: intro prose plus a generated lesson list. |
| `_layouts/`, `_includes/` | Six layouts, four includes. No theme gem. |
| `css/style.scss` | The whole stylesheet, hand-written, plain CSS in a `.scss` wrapper. |
| `assets/fonts/` | Self-hosted typefaces. No Google Fonts request. Their OFL notices are in `assets/fonts/OFL.txt`, which has to stay with them. |

## Adding a lesson

Write a Markdown file in `_posts/` named `YYYY-MM-DD-Short-Name.md`:

```yaml
---
layout: post
title: "What the lesson is called"
summary: One sentence, shown on every index page.
categories: ['Observing']
order: 11
tags: ['School-Teachers', 'Students', 'Hobbyists']
usemathjax: true      # only if the lesson contains LaTeX
---
```

`categories` takes exactly one name and it has to match a `category:` in
`_data/modules.yml` character for character. Get it wrong and the lesson still
builds — it just turns up in no module at all.

`order` is its place in that module, from 1. Take the next free number, or
renumber the module if your lesson belongs partway through. (Don't be tempted
to let the date do it: the dates are publication dates and six lessons share
one.)

The build checks both, so a mistake here fails the pull request rather than
quietly reordering the curriculum.

The full walkthrough, with images and video, is at
[`/newpost/`](https://wvurail.org/dspira-lessons/newpost/).

## Things worth knowing before you edit

- **GitHub Pages runs Jekyll 3.9**, via the `github-pages` gem — not the newest
  Jekyll. A filter or tag that needs anything newer fails the build *silently*:
  Pages emails the repository owner and keeps serving the last good copy, so the
  site simply stops updating. The Actions workflow in `.github/workflows/`
  builds against the same gem so this shows up as a red check instead.
- **MathJax loads only where `usemathjax: true` is set.** It also no longer
  treats a single `$` as an inline maths delimiter — that was matching the
  prices in the parts lists, so `$30 ... $54` turned everything between them
  into an equation.
- **Video**: put a YouTube URL alone on its own line and it becomes a responsive
  embed. With JavaScript off it stays a plain clickable link.
- **Images** belong in `images/`. Reference them as
  `{{ site.baseurl }}/images/name.png` — a bare relative path resolves against
  the lesson's own URL and 404s.
- There used to be a service worker here. It cached the stylesheet and the front
  page and had no `skipWaiting()`, so returning visitors could be served the old
  site indefinitely. It is gone, and `assets/js/lessons.js` actively unregisters
  any copy still installed in a visitor's browser.

## Local preview

```bash
bundle install
bundle exec jekyll serve
```
