# Python Data Visualization Guide

This repository provides a guide on visualizing data using both the `matplotlib` and `plotly` libraries in Python. These libraries offer a broad range of chart types and functionalities, from basic to advanced visualizations.

## Table of Contents

[Matplotlib](#matplotlib)
  - [Bar Charts](#bar-charts-matplotlib)
  - [Line Charts](#line-charts)
  - [Scatter Plots](#scatter-plots-matplotlib)
  - [Pie Charts](#pie-charts)
  - [Advanced Techniques](#advanced-techniques)
[Plotly](#plotly)
  - [Bar Charts](#bar-charts-plotly)
  - [Scatter Plots](#scatter-plots-plotly)


### Bar Charts (Matplotlib)


```python
import matplotlib.pyplot as plt

data = [5, 20, 15, 25, 10]
labels = ['A', 'B', 'C', 'D', 'E']

plt.bar(labels, data)
plt.show()
```

### Line Charts (Matplotlib)

```python
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 81, 86, 93, 87, 94, 78, 77, 85, 86]

plt.scatter(x, y)
plt.show()
```

### Pie Charts (Matplotlib)

```python
labels = 'A', 'B', 'C', 'D'
sizes = [15, 30, 45, 10]

plt.pie(sizes, labels=labels)
plt.show()
```

### Advanced Techniques (Matplotlib)

Multiple subplots - Create multiple charts in a single figure using 'subplot'.

```python
fig, axs = plt.subplots(2)
axs[0].plot(x, y)
axs[1].bar(labels, data)
plt.show()
```

Annotations - Use ax.annotate to add annotations to the plots.

```python
fig, ax = plt.subplots()
ax.plot(x, y)
ax.annotate('This is an annotation', xy=(3, 9), xytext=(4, 15),
            arrowprops=dict(facecolor='black', shrink=0.05))
```

Filling Between the Lines - The ax.fill_between method allows the area between two lines to be filled.

```python
x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [0, 1, 8, 27, 64]

fig, ax = plt.subplots()
ax.plot(x, y1, 'b', x, y2, 'r')
ax.fill_between(x, y1, y2, where=(y2>y1), facecolor='yellow', interpolate=True)
```

Super Titles - Use ax.suptitle to add a title to the entire figure when there are multiple subplots.

```python
fig.suptitle('This is a suptitle')
```

Setting axis limits - Set custom limits for x- and y-axes using ax.set_xlim and ax.set_ylim.

```python
ax.set_xlim(0, 6)
ax.set_ylim(0, 70)

```

Adding Text - Add custom text at any location on the plots using ax.text.

```python
ax.text(2, 6, 'Custom text here', style='italic')
```

### Bar Charts (Plotly)

```python
import plotly.graph_objs as go
from plotly import offline

data = [go.Bar(x=['A', 'B', 'C', 'D'], y=[10, 12, 15, 8])]
layout = go.Layout(title='Basic Bar Chart')
fig = go.Figure(data=data, layout=layout)

offline.plot(fig)
```

### Scatter Plots (Plotly)

```python
data = [go.Scatter(x=[1, 2, 3, 4], y=[10, 12, 15, 8], mode='markers')]
layout = go.Layout(title='Basic Scatter Plot')
fig = go.Figure(data=data, layout=layout)

offline.plot(fig)
```

For a detailed look into the charts, refer to the individual scripts in this repository. Feedback, issues, and suggestions are always welcome!
















