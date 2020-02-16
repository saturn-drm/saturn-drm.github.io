---
title: Failed to Import Module Installed through PIP
tags: Python
cover: https://i.loli.net/2020/01/08/IDs5oq2Pu1NCleL.png
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
modify_date: 2020-02-16
license: false
key: blog200216
---

# Question

I installed pandas and IPython with the command

`sudo pip3 install pandas / IPython`

The modules are in the list with the command

`pip3 list`

![200216.png](https://i.loli.net/2020/02/16/uObRqny8eEG4w3Q.png)

<!--more-->

However, when debugged in VSCode

```python
import IPython
```

there is the error of

`ModuleNotFoundError: No module named 'IPython'`

# Solution

When installing the modules, use the command

`sudo -H python -m pip install pandas / IPython`

---