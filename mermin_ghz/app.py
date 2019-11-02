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

cr = MerminGHZRandom()
co = MerminGHZOptimal()
quantum = MerminGHZQuantum()
allowed_inputs = [cr.to_bitstring(bits) for bits in cr.input_bits]

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Mermin-GHZ Game',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='A comparison of classical and quantum strategies.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Div(children=[
        html.Label('Choose valid inputs'),
        dcc.Dropdown(
            options=[
                {'label': bits, 'value': bits} for bits in allowed_inputs
            ],
            value='000'
        ),
        html.Label('Radio Items'),
        dcc.RadioItems(
            options=[
                {'label': 'Classical random', 'value': 'ran'},
                {'label': 'Classical optimal', 'value': 'opt'},
                {'label': 'Quantum', 'value': 'qm'}
            ],
            value='Classical random'
        )
    ])



])



if __name__ == '__main__':
    app.run_server(debug=True)
