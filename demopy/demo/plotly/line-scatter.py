import plotly.offline as py

py.init_notebook_mode(connected=False)
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

# Create traces
trace0 = go.Scatter(
    x=random_x,
    y=random_y0,
    mode='markers',
    name='markers'
)
trace1 = go.Scatter(
    x=random_x,
    y=random_y1,
    mode='lines+markers',
    name='lines+markers'
)
trace2 = go.Scatter(
    x=random_x,
    y=random_y2,
    mode='lines',
    name='lines'
)

data = [trace0, trace1, trace2]
py.iplot(data, filename='scatter-mode')
