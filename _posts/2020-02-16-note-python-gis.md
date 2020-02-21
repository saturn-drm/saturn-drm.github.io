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
modify_date: 2020-02-17
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

## polygon with hole

The output of `print (polygon)` is `POLYGON ((2.2 4.2, 7.2 -25.1, 9.26 -2.456, 2.2 4.2))`, which has double parentheses. That's because the polygon can contain holes.

### create the polygon with a hole

```python
# the points list of exterior polygon
points_exterior = [(-180, 90), (-180, -90), (180, -90), (180, 90)]

# the points list of hole polygon
# there could be multiple holes, thus input a list of holes
points_hole = [[(-170, 80), (-170, -80), (170, -80), (170, 80)]]

# syntax of the exterior polygon
polygon_exterior = Polygon(shell=points_exterior)

# syntax of the polygon with hole
polygon_with_hole = Polygon(shell=points_exterior, holes=points_hole)

print (polygon_exterior)
print (polygon_with_hole)
print (type(polygon_with_hole))
```

### output

```python
POLYGON ((-180 90, -180 -90, 180 -90, 180 90, -180 90))
POLYGON ((-180 90, -180 -90, 180 -90, 180 90, -180 90), (-170 80, -170 -80, 170 -80, 170 80, -170 80))
<class 'shapely.geometry.polygon.Polygon'>
```

# Geopandas / pandas

## Reading and Plotting a SHP

```python
import geopandas
import matplotlib.pyplot as plt

data = geopandas.read_file('./DataLesson2/DAMSELFISH_distributions.shp')

data.plot()
plt.show()
```

## Loop with Function iterrows()

### usage

The function iterrows() returns the index of each row, in addition to an object containing the row itself.

```python
for index, row in selection1.iterrows():
    poly_area = row['geometry'].area
    print('polygon area at index %i is: %.3f' %(index, poly_area))
```

### output
```python
polygon area at index 0 is: 19.396
polygon area at index 1 is: 6.146
polygon area at index 2 is: 2.697
polygon area at index 3 is: 87.461
polygon area at index 4 is: 0.001
```

## Function groupby()

The function gives an object called `DataFrameGroupBy`, similar to list of keys and values (in a dictionary) that we can iterate over.

```python
grouped = data.groupby('BINOMIAL')
for key, values in grouped:
    individual_fish = values
```

## Function value_counts()

[Official Documentations](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.value_counts.html?highlight=value_counts#pandas.Index.value_counts)

### value_counts() in a column

```python
print(acc['Suitable_area'].value_counts())
#type(acc) = geodataframe
```

### Output
```python
0    13011
1        9
```

# OSMnx

## Documententation

### osmnx.plot.plot_graph

```
Parameters:
G, bbox=None, fig_height=6, fig_width=None, margin=0.02, axis_off=True, equal_aspect=False, bgcolor='w', show=True, save=False, close=True, file_format='png', filename='temp', dpi=300, annotate=False, node_color='#66ccff', node_size=15, node_alpha=1, node_edgecolor='none', node_zorder=1, edge_color='#999999', edge_linewidth=1, edge_alpha=1, use_geom=True
```

**Returns: fig, ax**

Return type: tuple

[Documentation page](https://osmnx.readthedocs.io/en/stable/osmnx.html#osmnx.plot.plot_graph)

---