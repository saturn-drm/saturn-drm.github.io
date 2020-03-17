---
title: Scroll Smooth in Safari
tags: Website
mode: normal
sidebar:
  nav: side-blog
show_title: true
show_edit_on_github: false
show_date: false
show_tags: true
pageview: false
comment: true
mathjax: true
mathjax_autoNumber: true
mermaid: true
chart: true
lightbox: false
show_author_profile: true
show_subscribe: true
sharing: true
modify_date: 2020-03-17
license: false
key: blogscrollsmooth
---

# Question

When editing my website, I wanted to scroll smoothly between sections, and when scrolling to top.

<!--more-->

# Solution 1

Basically, I found the simply way to achieve this with CSS properties:

```CSS
scroll-behavior: smooth;
```

However, I noticed that Safari didn't support the CSS property "scroll-behavior". So I need a special way to achieve this.

# Solution 2

I found the jQuery script to achieve such design.

```js
<script src="https://code.jquery.com/jquery-3.4.1.min.js"
    integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>

<script>
    $(document).ready(function () {
        $("a").on('click', function (event) {

            if (this.hash !== "") {
                event.preventDefault();

                var hash = this.hash;

                $('html, body').animate({
                    scrollTop: $(hash).offset().top
                }, 800, function () {

                    window.location.hash = hash;
                });
            }
        });
    });
</script>
```

---