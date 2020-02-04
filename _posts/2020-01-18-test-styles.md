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
modify_date: 2020-02-04
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

### Javascript Object

![anime03-js-selector.gif](https://i.loli.net/2020/02/04/pAjoGtaxfkinMlq.gif)

* HTML

```html
<div class="main">
	<p class="battery-log"></p>
</div>
```

* CSS

```css
.main {
  position: relative;
  justify-content: center;
  width: auto;
  height: auto;
  text-align: center;
  left: 50vw;
  top: 50vh;
}

.battery-log {
  font-size: 2rem;
  color: #2c3e50;
}
```

* Javascript

```js
var logEL = document.querySelector('.battery-log');

var battery = {
  charged: '0%',
  cycles: 120   
}

var animation = anime({
  targets: battery,
  charged: '100%',
  cycles: 130,
  round: 1,
  loop: true,
  easing: 'linear',
  update: function(){
    logEL.innerHTML = JSON.stringify(battery);
  }
});
```

Click to [ANIME WITH JAVSCRIPT OBJECT](../zh/anime03-js-selector.html)

## Practice - Proporties

### CSS Proporties

> Most CSS properties will cause layout changes or repaint, and will result in choppy animation. Prioritize opacity and CSS transforms as much as possible.

![anime04-css-proporties.gif](https://i.loli.net/2020/02/04/2usOtHAhaVNj9Pw.gif)

* HTML

```html
<div class="main"></div>
```

* CSS

```css
.main {
  position: relative;
  justify-content: center;
  text-align: center;
  left: 20vw;
  top: 50vh;
  width: 5vw;
  height: 5vw;
  border: 0rem;
  background-color: #2c3e50;
}
```

* Javascript

```js
anime({
  targets: '.main',
  translateX: ['0', '60vw'],
  // start from the original position to 60vw right of the original
  backgroundColor: '#fee3e1',
  borderRadius: ['0%', '50%'],
  easing: 'easeInOutQuad',
 loop: true
});
```

Click to [ANIME WITH CSS PROPORTIES](../zh/anime04-css-proporties.html)

## Test I

Click to [SVG LINE DRAWING](../zh/test-anime-2.html)