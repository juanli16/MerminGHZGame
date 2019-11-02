import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import sys
from mermin_ghz_classical_random import MerminGHZRandom
from mermin_ghz_classical_optimal import MerminGHZOptimal
from mermin_ghz_quantum import MerminGHZQuantum


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}



app.layout = html.Div()

random = MerminGHZRandom()
optimal = MerminGHZOptimal()
quantum = MerminGHZQuantum()
allowed_inputs = random.input_bits
print(allowed_inputs)

if __name__ == '__main__':
    app.run_server(debug=True)
