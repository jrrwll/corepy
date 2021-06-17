import plotly.offline as py

py.init_notebook_mode(connected=False)
import pandas as pd

# Scatter plot with multiple traces
df = pd.read_csv('http://www.stat.ubc.ca/~jenny/notOcto/STAT545A/examples/gapminder/data/gapminderDataFiveYear.txt',
                 sep='\t')
df2007 = df[df.year == 2007]
df1952 = df[df.year == 1952]
df.head(2)
fig = {
    'data': [
        {
            'x': df2007.gdpPercap,
            'y': df2007.lifeExp,
            'text': df2007.country,
            'mode': 'markers',
            'name': '2007'},
        {
            'x': df1952.gdpPercap,
            'y': df1952.lifeExp,
            'text': df1952.country,
            'mode': 'markers',
            'name': '1952'}
    ],
    'layout': {
        'xaxis': {'title': 'GDP per Capita', 'type': 'log'},
        'yaxis': {'title': "Life Expectancy"}
    }
}
# IPython notebook
py.iplot(fig, filename='multiple-scatter')
# url = py.plot(fig, filename='pandas/multiple-scatter')

# Scatter plot with grouped traces
df = pd.read_csv('http://www.stat.ubc.ca/~jenny/notOcto/STAT545A/examples/gapminder/data/gapminderDataFiveYear.txt',
                 sep='\t')
df2007 = df[df.year == 2007]
df1952 = df[df.year == 1952]
df.head(2)
fig = {
    'data': [
        {
            'x': df[df['year'] == year]['gdpPercap'],
            'y': df[df['year'] == year]['lifeExp'],
            'name': year, 'mode': 'markers',
        } for year in [1952, 1982, 2007]
    ],
    'layout': {
        'xaxis': {'title': 'GDP per Capita', 'type': 'log'},
        'yaxis': {'title': "Life Expectancy"}
    }
}
# IPython notebook
py.iplot(fig, filename='grouped-scatter')
# url = py.plot(fig, filename='pandas/grouped-scatter')

# Single scatter plot with cufflinks
import cufflinks as cf

cf.set_config_file(offline=False, world_readable=True, theme='ggplot')
df = pd.read_csv('http://www.stat.ubc.ca/~jenny/notOcto/STAT545A/examples/gapminder/data/gapminderDataFiveYear.txt',
                 sep='\t')
df2007 = df[df.year == 2007]
df1952 = df[df.year == 1952]
df.head(2)
df2007.iplot(kind='scatter', mode='markers', x='gdpPercap', y='lifeExp', filename='simple-scatter')
