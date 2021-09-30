import plotly.offline as py

py.init_notebook_mode(connected=False)

import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers'
)

data = [trace]

plot_url = py.plot(data, filename='basic-scatter.html')
print(plot_url)
