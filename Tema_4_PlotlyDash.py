import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
df = pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y': [10, 20, 25, 30]
})
fig = px.line(df, x='x', y='y')
app.layout = html.Div(children=[
    html.H1(children='Exemplo de Dashboard com Dash'),
    dcc.Graph(id='example-graph',
              figure=fig)
])
if __name__ == '__main__':
    app.run(debug=True)
