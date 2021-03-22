---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---
{% for post in site.posts limit:1 %}
{{ post.content }}
{% endfor %}

<a href="/post_index">Índex de resums</a>
