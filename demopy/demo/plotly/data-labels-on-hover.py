import plotly.offline as py

py.init_notebook_mode(connected=False)
import plotly.graph_objs as go
import numpy as np
import pandas as pd

l = []
y = []
data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")
# Setting colors for plot.
N = 53
c = ['hsl(' + str(h) + ',50%' + ',50%)' for h in np.linspace(0, 360, N)]

for i in range(int(N)):
    y.append((2000 + i))
    trace0 = go.Scatter(
        x=data['Rank'],
        y=data['Population'] + (i * 1000000),
        mode='markers',
        marker=dict(size=14,
                    line=dict(width=1),
                    color=c[i],
                    opacity=0.3
                    ), name=y[i],
        text=data['State'])  # The hover text goes here...
    l.append(trace0)

layout = go.Layout(
    title='Stats of USA States',
    hovermode='closest',
    xaxis=dict(
        title='Population',
        ticklen=5,
        zeroline=False,
        gridwidth=2,
    ),
    yaxis=dict(
        title='Rank',
        ticklen=5,
        gridwidth=2,
    ),
    showlegend=False
)
fig = go.Figure(data=l, layout=layout)
py.iplot(fig)
