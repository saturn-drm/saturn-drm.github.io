---
title: Enable Jupyter in VSCode
modify date: 2020-02-22
tags: [Python]
head image: /assets/img/covers/codingcover.jpg
---

> Modify date: 2020-02-22

# Usage

## Start Jupyter in VSCode

![jupyter-1](../../../assets/img/01coding/jupyter-1.png)

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

![jupyter-2](../../../assets/img/01coding/jupyter-2.png)

---

# Problem in Setting

Python Interactive shows error of **Jupyter Server: Unconnected**.

## Solution

Install module of **notebook**

```python
sudo pip3 install notebook
```

---