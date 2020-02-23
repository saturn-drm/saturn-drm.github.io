---
title: Enable Jupyter in VSCode
tags: Python
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
modify_date: 2020-02-22
license: false
key: blogjupyter
---

# Usage

## Start Jupyter in VSCode

![jupyter-1](../assets/images/blog/jupyter-1.png)

<!--more-->

Add `#%%` to the first line of py file. The **Run Cell**, **Run Below**, and **Debug Cell** function will be added to VSCode.

**Example**

```python
# %%
import osmnx
import pandas
import matplotlib.pyplot
import geopandas
```

## Python Interactive

Use **Shift + Enter** or command **Run Cell** to start Python Interactive.

![jupyter-2](../assets/images/blog/jupyter-2.png)

---

# Problem in Setting

Python Interactive shows error of **Jupyter Server: Unconnected**.

## Solution

Install module of **notebook**

```python
sudo pip3 install notebook
```

---