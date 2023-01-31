import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from .side_bar import sidebar

dash.register_page(__name__)

def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    html.H3('Air Quality monitoring and modeling in Bogotá, D.C., Colombia', style={'textAlign':'center'}),
                    html.Hr(),
                    dcc.Markdown('**Abstract:** d\n'
                                 'relationship with lung cancer. Despite its potential health impacts, few studies have been carried out to\n'
                                 'assess this public health problem in countries where RC measurements and research are scarce. This study aims\n'
                                 'to contribute to the bridging of the baseline information gap by using inferential statistic methods to estimate\n'
                                 'indoor RC spatial distribution and building an easy-to-use [webapp](https://indoorrn-modelingapp.onrender.com/) for RC modeling.'),
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])