---
title: Test Style
tags: Website
mode: normal
sidebar:
  nav: side-blog
show_title: false
show_edit_on_github: false
show_date: false
show_tags: true
pageview: false
comment: false
mathjax: false
mathjax_autoNumber: false
mermaid: false
chart: false
lightbox: false
show_author_profile: false
show_subscribe: false
sharing: false
modify_date: 2020-02-02
license: false
key: test-style
---

# Pure CSS Styles

## Blend

![style-blend.gif](https://i.loli.net/2020/02/02/hgZFjmUrxpYwe1J.gif)

<!--more-->

Click to [Style Blend](../zh/test-page.html)

# Anime.js

## Practice - Targets

### CSS Selector

![anime01-css-selector.gif](https://i.loli.net/2020/02/03/OoDMXtlkySvuZBe.gif)

* HTML

```html
<div class="small-block-1"></div>
```

* CSS

```css
div.small-block-1{
  position: absolute;
  left: 22.5vw;
  top: calc(50vh - 2.5vw);
  width: 5vw;
  height: 5vw;
  border: 0rem;
  border-radius: 1vw;
  background-color: #2c3e50;
}
```

* Javascript

```js
var animation = anime({
  targets: ['.small-block-1'],
  translateX: '50vw',
  loop: true
});
```

Click to [ANIME WITH CSS SELECTOR](../zh/anime01-css-selector.html)

### DOM List Selector

![anime02-mod-selector.gif](https://i.loli.net/2020/02/03/wPvgz3TdDlNWpif.gif)

> DOM Node

```js
targets: el.querySelector('.item')
```

> Node List

```js
targets: el.querySelectorAll('.item')
```

* HTML

```html
<div class="small-block a"></div>
<div class="small-block b"></div>
<div class="small-block c"></div>
```

* CSS

```css
.small-block{
  position: absolute;
  left: 22.5vw;
  width: 5vw;
  height: 5vw;
  border: 0rem;
  border-radius: 1vw;
  background-color: #2c3e50;
}

.a {
  top: calc(50vh - 2.5vw - 6vw);
}

.b {
  top: calc(50vh - 2.5vw);
}

.c {
  top: calc(50vh - 2.5vw + 6vw);
}
```

* Javascript

```js
var elements = document.querySelectorAll('.small-block');
var animation = anime({
  targets: elements,
  translateX: '50vw',
  loop: true
});
```

Click to [ANIME WITH DOM SELECTOR](../zh/anime02-dom-selector.html)

## Test I

Click to [SVG LINE DRAWING](../zh/test-anime-2.html)