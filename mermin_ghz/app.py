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

    html.Div(style={'width': '12%', 'margin-left': 'auto', 'margin-right': 'auto', 'padding': '10px'}, children=[
        html.Button("Let's play", id='strategy_demo')
    ]),

    html.Div(id='players', style={'width':'600px', 'height': '270px', 'margin-left':'auto','margin-right':'auto', 'padding': '10px'}, children=[
        html.Div(id='strategy_demo_images_alice', style={'float': 'left', 'width': '200px', 'height': '200px'}, children=[
            html.Img(id='Alice', style={'width': '100%', 'border-radius': '50%'}, src='assets/alice.png'),
            html.H2(id='Alice_output', children='0', style={'text-align': 'center'})
        ]),
        html.Div(id='strategy_demo_images_bob', style={'float': 'left', 'width': '200px', 'height': '200px'}, children=[
            html.Img(id='Bob', style={'width': '100%', 'border-radius': '50%'}, src='assets/bob.png'),
            html.H2(id='Bob_output', children='0', style={'text-align': 'center'})
        ]),
        html.Div(id='strategy_demo_images_charlie', style={'float': 'left', 'width': '200px', 'height': '200px'}, children=[
            html.Img(id='Charlie', style={'width': '100%', 'border-radius': '50%'}, src='assets/charlie.png'),
            html.H2(id='Charlie_output', children='0', style={'text-align': 'center'})
        ])
    ]),
    
    html.Div(id='strategy_demo_color', style={'width': '600px', 'margin-left': 'auto', 'margin-right': 'auto', 'padding': '10px', 'text-align': 'center'}, children=[
        html.H3(id='strategy_demo_result')
    ])
])

@app.callback(
    [Output('Alice_output', 'children'),
    Output('Bob_output', 'children'),
    Output('Charlie_output', 'children'),
    Output('strategy_demo_result', 'children')],
    [Input('strategy_demo', 'n_clicks'),
     Input('input_bit', 'value'),
     Input('strategy', 'value')])
def update_strategy_demo(n_click, input_bit, strategy):
    if n_click is not None:
        input_bit = [int(x) for x in input_bit]
        if strategy == 'ran':
            _, output_bits = cr.run(input_bit)
        elif strategy == 'opt':
            _, output_bits = co.run(input_bit)
        else:
            _, output_bits = qm.run(1, input_bit)
            output_bits = output_bits[0]
        # test with verify function to see if won
        if cr.verify(input_bit, output_bits) is True:
            result  = 'Winner Winner, Chicken Dinner'
        else:
            result = 'Loser Loser, Nyquil Boozer'
        output_bits = cr.to_bitstring(output_bits)
        #n_click = 0
        return output_bits[0], output_bits[1], output_bits[2], result
    else:
        return '', '', '', ''

if __name__ == '__main__':
    app.run_server(debug=True)
