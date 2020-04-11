---
title: Scroll Smooth in Safari
modify date: 2020-03-17
tags: [Website]
head image: /assets/img/covers/codingcover.jpg
---

> Modify date: 2020-03-17

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

```html
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