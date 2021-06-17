# import plotly.plotly as py
import plotly.offline as py

py.init_notebook_mode(connected=False)
import plotly.tools as tls

import matplotlib.pyplot as plt
import numpy as np

# Basic Scatter Plot
fig, ax = plt.subplots()
ax.scatter(np.linspace(-1, 1, 50), np.random.randn(50))
plotly_fig = tls.mpl_to_plotly(fig)
py.iplot(plotly_fig, filename='mpl-basic-scatter-plot')

# Line and Scatter Plot
x = [1, 2, 3, 4]
y = [3, 4, 8, 6]
plt.plot(x, 'o')
plt.plot(y)
fig = plt.gcf()
plotly_fig = tls.mpl_to_plotly(fig)
py.iplot(plotly_fig, filename='mpl-scatter-line')
line = plt.figure()

# Adding Line To Matplotlib Scatter Plot
np.random.seed(5)
x = np.arange(1, 101)
y = 20 + 3 * x + np.random.normal(0, 60, 100)
plt.plot(x, y, "o")
# draw vertical line from (70,100) to (70, 250)
plt.plot([70, 70], [100, 250], 'k-', lw=2)
# draw diagonal line from (70, 90) to (90, 200)
plt.plot([70, 90], [90, 200], 'k-')
plotly_fig = tls.mpl_to_plotly(line)
py.iplot(plotly_fig, filename='mpl-add-line-plot')

# Matplotlib Scatter Colors And Symbols
fig, ax = plt.subplots()
num = 1000
s = 121
x1 = np.linspace(-0.5, 1, num) + (0.5 - np.random.rand(num))
y1 = np.linspace(-5, 5, num) + (0.5 - np.random.rand(num))
x2 = np.linspace(-0.5, 1, num) + (0.5 - np.random.rand(num))
y2 = np.linspace(5, -5, num) + (0.5 - np.random.rand(num))
x3 = np.linspace(-0.5, 1, num) + (0.5 - np.random.rand(num))
y3 = (0.5 - np.random.rand(num))
ax.scatter(x1, y1, color='r', s=2 * s, marker='^', alpha=.4)
ax.scatter(x2, y2, color='b', s=s / 2, alpha=.4)
ax.scatter(x3, y3, color='g', s=s / 3, marker='s', alpha=.4)
plotly_fig = tls.mpl_to_plotly(fig)
py.iplot(plotly_fig, filename='mpl-scatter-color-symbol')

# Scatter Plot With Duplicate Points
alpha = plt.figure()
data = [i for i in range(8) for j in range(np.random.randint(10))]
x, y = np.array(data), np.array(data)
plt.scatter(x, y, alpha=.1, s=400)
plotly_fig = tls.mpl_to_plotly(alpha)
py.iplot(plotly_fig, filename='mpl-duplicate-points')

# Color And Marker Options
from pylab import *

scatter = plt.figure()
colors = (i + j for j in 'o<.' for i in 'bgrcmyk')
labels = 'one two three four five six seven eight nine ten'.split()
x = linspace(0, 2 * pi, 3000)
d = (2 + random((2, 3000))) * c_[sin(x), cos(x)].T
lg = []
for i, l, c in zip(range(10), labels, colors):
    start, stop = i * 300, (i + 1) * 300
    handle = plot(d[0, start:stop], d[1, start:stop], c, label=l)
    lg.append(handle)

plotly_fig = tls.mpl_to_plotly(scatter)
py.iplot(plotly_fig, filename='mpl-color-marker-optns')

# Scatter Plot With Legend And Label
colors = ['b', 'c', 'y', 'm', 'r']
lo = plt.scatter(random(10), random(10), marker='x', color=colors[0])
ll = plt.scatter(random(10), random(10), marker='o', color=colors[0])
l = plt.scatter(random(10), random(10), marker='o', color=colors[1])
a = plt.scatter(random(10), random(10), marker='o', color=colors[2])
h = plt.scatter(random(10), random(10), marker='o', color=colors[3])
hh = plt.scatter(random(10), random(10), marker='o', color=colors[4])
ho = plt.scatter(random(10), random(10), marker='x', color=colors[4])
text = iter(['Low Outlier', 'LoLo', 'Lo', 'Average', 'Hi', 'HiHi', 'High Outlier'])
mpl_fig = plt.gcf()
plotly_fig = tls.mpl_to_plotly(mpl_fig)

for dat in plotly_fig['data']:
    t = text.__next__()
    dat.update({'name': t, 'text': t})

plotly_fig['layout']['showlegend'] = True
py.iplot(plotly_fig, filename='mpl-scatter-legend-label')

# Colored Matplotlib Line Chart
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
fig = plt.gcf()
plotly_fig = tls.mpl_to_plotly(fig)
py.iplot(plotly_fig, filename='mpl-colored-line')
