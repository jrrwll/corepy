import plotly.graph_objs as go
import plotly.offline as py

py.init_notebook_mode(connected=False)

import numpy as np

trace1 = go.Scatter(
    y=np.random.randn(500),
    mode='markers',
    marker=dict(
        size=16,
        color=np.random.randn(500),  # set color equal to a variable
        colorscale='Viridis',
        showscale=True
    )
)
data = [trace1]

py.iplot(data, filename='scatter-plot-with-colorscale')
