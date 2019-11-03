import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
# Actual game
from mermin_ghz_classical_random import MerminGHZRandom
from mermin_ghz_classical_optimal import MerminGHZOptimal
from mermin_ghz_quantum import MerminGHZQuantum

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css','https://fonts.googleapis.com/css?family=IBM+Plex+Sans&display=swap']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}

app.title = 'Mermin GHZ Game'

cr = MerminGHZRandom()
co = MerminGHZOptimal()
qm = MerminGHZQuantum()
allowed_inputs = [cr.to_bitstring(bits) for bits in cr.input_bits]

app.layout = html.Div(style={'backgroundColor': colors['background'],'font-family': 'IBM Plex Sans'}, children=[
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

    html.Div(style={'width': '12%','margin-left': 'auto', 'margin-right': 'auto', 'padding': '10px'}, children=[
        html.Label('Choose valid inputs'),
        dcc.Dropdown(
            id='input_bit',
            options=[
                {'label': bits, 'value': bits} for bits in allowed_inputs
            ],
            value='000'
            )]
    ),

    html.Div(style={'width': '12%','margin-left': 'auto', 'margin-right': 'auto', 'padding': '10px'}, children=[
        html.Label('Strategy'),
        dcc.RadioItems(
            id='strategy',
            options=[
                {'label': 'Classical random', 'value': 'ran'},
                {'label': 'Classical optimal', 'value': 'opt'},
                {'label': 'Quantum', 'value': 'qm'}
            ],
            value='Classical random'
        )
    ]),

#    html.Div(style={'width': '12%', 'margin-left': 'auto', 'margin-right': 'auto', 'padding': '10px'}, children=[
#        html.Button("Let's play", id='strategy_demo')
#    ]),

    html.Div(id='players', style={'width':'600px','margin-left':'auto','margin-right':'auto', 'padding': '10px'}, children=[
        html.Div(id='strategy_demo_images_alice', style={'float': 'left', 'width': '200px'}, children=[
            html.Img(id='Alice', style={'width': '100%', 'border-radius': '50%'}, src='assets/alice.png'),
            html.H2(children='0', style={'text-align': 'center'})
        ]),
        html.Div(id='strategy_demo_images_bob', style={'float': 'left', 'width': '200px'}, children=[
            html.Img(id='Bob', style={'width': '100%', 'border-radius': '50%'}, src='assets/bob.png'),
            html.H2(children='0', style={'text-align': 'center'})
        ]),
        html.Div(id='strategy_demo_images_charlie', style={'float': 'left', 'width': '200px'}, children=[
            html.Img(id='Charlie', style={'width': '100%', 'border-radius': '50%'}, src='assets/charlie.png'),
            html.H2(children='0', style={'text-align': 'center'})
        ])
    ])
])

"""
@app.callback(
    Output('strategy_demo', 'figure'),
    [Input('input_bit', 'value'),
     Input('strategy', 'value')])
"""
def update_strategy_demo(input_bit, strategy):
    if strategy == 'ran':
        input_bit, output_bits = cr.run(input_bit)
    elif strategy == 'opt':
        input_bit, output_bits = cr.run(input_bit)
    else:
        input_bit, output_bits = qm.run(input_bit)
    return input_bit, output_bits

if __name__ == '__main__':
    app.run_server(debug=True)
