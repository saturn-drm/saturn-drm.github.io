---
title: Notes in Python GIS
tags: [Python, GIS]
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
key: blogGISNote
---

# Shapely

## Methods to access Geometry Type

### shapely function - type

> string

```python
poly_type1 = poly1.type
print (poly_type1)
>> Polygon
```

<!--more-->

### shapely function - geom_type

> string

```python
poly_type2 = poly1.geom_type
print (poly_type2)
>> Polygon
```

### Python function - type

> Python class format

```python
poly_type3 = type(poly1)
print (poly_type3)
>> <class 'shapely.geometry.polygon.Polygon'>
```

---