import dash_core_components as dcc
import dash_html_components as html


def get_layout():
    return html.Div(children=[
        html.H1(children='COVID-19 dashboard'),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1,2,3], 'y': [1,3,2], 'type': 'bar', 'name': 'A'},
                    {'x': [1,2,3], 'y': [2,1,1], 'type': 'bar', 'name': 'B'},
                ],
                'layout': {
                    'title': 'test graph'
                }
            }
        )
    ])


def world_map(df):
    """
    World map graph with bubbles to show data frequency.
    """
