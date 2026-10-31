---
title: Notes
description: "Programming and research notes."
permalink: /notes/
redirect_from:
  - /archive.html
  - /2021/03/08/blog-post-title-from-file-name.html
section: notes
---
{% if site.posts.size > 0 %}
{% assign years = site.posts | group_by_exp: 'post', 'post.date | date: "%Y"' %}
{% for year in years %}
<section class="archive-year" aria-label="Notes from {{ year.name }}">
  <h2 class="year-heading">{{ year.name }}</h2>
  {% include note-list.html posts=year.items %}
</section>
{% endfor %}
{% else %}
<p class="empty-note">No notes published yet.</p>
{% endif %}
