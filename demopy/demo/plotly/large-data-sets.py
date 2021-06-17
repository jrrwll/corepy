import plotly.offline as py

py.init_notebook_mode(connected=False)
import plotly.graph_objs as go
import numpy as np

N = 100000
trace = go.Scattergl(
    x=np.random.randn(N),
    y=np.random.randn(N),
    mode='markers',
    marker=dict(
        color='#FFBAD2',
        line=dict(width=1)
    )
)
data = [trace]
py.iplot(data, filename='compare_webgl')
