import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
df = pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y': [10, 20, 25, 30]
})
app.layout = html.Div(children=[
    html.H1(children='Dashboard Interativo com Callback'),
    dcc.Input(id='input-number', type='number', value=1),
    dcc.Graph(id='output-graph')
])
@app.callback(
    Output('output-graph', 'figure'),
    Input('input-number', 'value')
)
def update_graph(input_value):
    filtered_df = df[df['x'] <= input_value]
    fig = px.line(filtered_df, x='x', y='y')
    return fig
if __name__ == '__main__':
    app.run(debug=True)