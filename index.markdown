---
layout: default
---

<div class="content-wrapper">
  <header class="post-header">
    <h1>Benvinguts al Diari de Rol</h1>
  </header>

  <p>Aquest és el diari d'un grup d'aventurers als mons de Dungeons & Dragons.</p>

  <h2>Última sessió</h2>

  {% for post in site.posts limit:1 %}
  <article>
    <p class="post-meta">{{ post.date | date: "%d %B %Y" }} {% if post.tags %}&middot; {{ post.tags | join: ", " }}{% endif %}</p>
    {{ post.content | markdownify }}
  </article>
  {% endfor %}

  <a class="back-link" href="{{ '/post_index' | relative_url }}">Veure totes les sessions &#8594;</a>
</div>
