---
layout: page
title: DSPIRA lesson updates
permalink: /updates/
eyebrow: Stay connected
lead: Browse the latest lessons, or follow new posts in your RSS reader.
meta_description: "Read the latest DSPIRA lessons and follow new posts in your RSS reader. Find the feed address and simple subscription instructions."
---

## Follow new lessons

RSS lets a feed reader collect new posts from websites you follow.
The DSPIRA feed includes the ten most recently published lessons.

1. Copy the feed address below.
2. Open your RSS reader and choose its option to add a feed or subscription.
3. Paste the address and confirm the subscription.

<label for="rss-feed-address" class="form-label fw-bold">RSS feed address</label>
<input id="rss-feed-address" class="form-control mb-3" type="url" value="{{ '/feed.xml' | absolute_url }}" readonly aria-describedby="rss-feed-help">
<p id="rss-feed-help">The feed uses XML for RSS readers. This page displays the latest lesson links for reading in your browser.</p>

[Open the XML feed for an RSS reader]({{ '/feed.xml' | relative_url }})

## Latest lessons

<ul class="list-unstyled">
{% for post in site.posts limit:10 %}
  <li class="mb-3">
    <a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a><br>
    <span class="small">Published <time datetime="{{ post.date | date: '%Y-%m-%d' }}">{{ post.date | date: '%B %-d, %Y' }}</time></span>
  </li>
{% endfor %}
</ul>

[Browse all lessons]({{ '/all/' | relative_url }})
