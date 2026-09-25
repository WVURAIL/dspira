# DSPIRA lessons

The lesson site for **Digital Signal Processing in Radio Astronomy** — free
material on building and using a horn radio telescope, written by the high
school teachers who did it.

Live at <https://wvurail.org/dspira/>, built by GitHub Pages from the
`main` branch. The site is moving to <https://rail.wvu.edu/dspira/>
together with the lab site, and the `wvu` branch is the build for the
University domain: the WVU Design System, the standard masthead and footer, and
the University's accessibility bar. The checklist for the move is
`.github/CUTOVER.md` in the lab site's repository, `wvurail.github.io` — the
organisation site, whose domain this one inherits. Merging `wvu` into `main`
lands with the cutover commit and not before: `main` is what wvurail.org
serves, and the merge waits on the University's review approval.

## How it is put together

| Path | What it is |
|---|---|
| `_posts/` | The lessons - 51 at last count. One Markdown file each. |
| `_data/modules.yml` | The module order and blurbs. Drives the front page and `/all/`. |
| `_data/nav.yml` | Site navigation. Edit here, every page follows. |
| `_data/forum.yml` | The forum rooms: one entry per room, naming the GitHub Discussions category it links to. |
| `_config.yml` | Site settings, and the `contact:` block — address, phone, fax, email — that the footer prints on every page. |
| `categories/*/index.md` | One page per module: intro prose plus a generated lesson list. |
| `_layouts/`, `_includes/` | The layouts, and the includes: the head, the University's masthead and footer, and `icon.html`, the site's inline SVG icons. No theme gem. |
| `css/lessons.scss` | The residual stylesheet: the few rules the Design System does not supply, plain CSS in a `.scss` wrapper. Everything else the pages wear is the Design System's. |
| `assets/js/lessons.js` | The video embeds, the filter on `/all/`, and the service-worker clean-up described below. The mobile menu is the Design System's own script, not this. |
| `tools/` | The link, layout, maths and contrast checks CI runs. `tools/README.md` explains each. |

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

Headings in the lesson start at `##`; the layout supplies the `h1`, and every
page gets exactly one. A link becomes a button with `{: .btn .btn-wvu-blue}`
after it — Design System classes, so it matches the rest of the University's
pages — and `.btn-wvu-gold` is for the one primary action on a page, if there
is one. Write it that way, not the old `{: .button}`.

The full walkthrough, with images and video, is at
[`/newpost/`](https://wvurail.org/dspira/newpost/).

## The Design System

The look is the [WVU Design System](https://designsystem.wvu.edu/), version 3:
a Bootstrap 5.3 fork on a 24-column grid (`col-24` is full width, `col-lg-16`
two thirds). The stylesheet and the Adobe Fonts faces load from
designsystem.wvu.edu and use.typekit.net, exactly as
<https://designsystem.wvu.edu/getting-started> documents — two `<link>` lines
in the head include, nothing vendored, no fonts directory. That is also why a
local preview wants the internet: without it the pages render unstyled.

- **The masthead and footer are the University's common elements**, the same
  ones the lab site carries. The footer's address, phone, fax and email come
  from the `contact:` block in `_config.yml`, so there is one place to change
  them. The footer retains the copyright line. The September 2026 design review
  removed the Equal Opportunity/Affirmative Action sentence.
- **Some obvious class names do not exist** and silently do nothing. The
  off-white band is `bg-wvu-not-quite-white` (there is no
  `bg-wvu-neutral-subtle`), and the display face is `antonia-light` /
  `antonia-regular` / `antonia-italic` (`antonia-variable` is the font-family
  name, not a utility).
- **Icons are inline SVG**, from `_includes/icon.html`. The Font Awesome kit
  the Design System documentation lists is account-bound and returns 403 from
  any origin that is not on its allowlist, so it is not used here.
- **Body text is dark gray on white**, as the University's standard requires,
  and the bar is WCAG 2.1 AA with no A or AA errors. CI measures contrast and
  horizontal overflow (`tools/`); the rest is by hand: one `h1` per page and
  headings that cascade, `alt` on every image, links in running text
  underlined, no inline event handlers, `aria-current` on the current
  navigation item.
- **The forum pages link out.** `/forum/` and its rooms are plain links to the
  repository's GitHub Discussions categories, listed in `_data/forum.yml`. The
  giscus comment boxes are gone: the University does not currently allow a
  forum on one of its pages, and the boxes were only ever fronting those same
  Discussions.
- **Links.** Every internal href goes through `relative_url`, so the whole site
  can be served under another subpath for staging. Links to the lab site on
  the same host — `/`, `/education/`, `/lightwork/`, `/accessibility/` — are
  root-absolute on purpose and do not get the filter.

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
# open http://localhost:4000/dspira/
```
