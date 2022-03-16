import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv('data.csv')

fig = go.Figure(
    go.Scatter(x=df.groupby('level')['attempt'].mean(),
    y=['level1','level2','level3','level4'],
    orientation='h')
    )

fig.show()

