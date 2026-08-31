---
layout: page
title: Who these are written for
permalink: /user-levels/
eyebrow: Audience
lead: Written for high school teachers, and usable well beyond them.
---

Every lesson here was written by a teacher, for a classroom. That is the level
they are pitched at: a high school science or engineering class, no prior radio
astronomy assumed.

That has turned out to be about the right level for two other groups as well.
Students work through most of them directly, and amateur radio astronomers and
hobbyists use them to build the same instrument outside a school entirely.

Because nearly every lesson suits all three, filtering by audience does not
narrow things much. It is usually faster to
[browse every lesson]({{ '/all/' | relative_url }}) or read
[the full list]({{ '/all/' | relative_url }}).

If you would rather filter anyway:

{% for tag in site.tags %}
- [{{ tag[0] | replace: '-', ' ' }}]({{ tag[0] | slugify | prepend: '/tags/' | append: '/' | relative_url }}) — {{ tag[1] | size }} lessons
{% endfor %}
