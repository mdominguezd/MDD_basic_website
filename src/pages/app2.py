import dash_bootstrap_components as dbc
from .side_bar import sidebar

import dash
from dash import Dash, dcc, html, callback, callback_context, dash_table
import dash_daq as daq
from dash.dependencies import Input, Output, State

import plotly.express as px
import plotly.graph_objects as go

import geopandas as gpd
import pandas as pd

import statsmodels.api as sm
from sklearn.neighbors import KNeighborsRegressor

from .Functions import read_data, fit_regression, get_metrics, get_error_n_predicted_GeoJSON

dash.register_page(__name__, title = 'ML_Project')

# Read the data that will be used
X_train, X_test, y_train, y_test = read_data()
# To avoid reading the geojson everytime we update the map
nuts2 = gpd.read_file('https://gisco-services.ec.europa.eu/distribution/v2/nuts/geojson/NUTS_RG_01M_2016_4326_LEVL_2.geojson')

# Style parameters
color = 'darkgreen'
font_s = {'font-family' : 'bahnschrift'}

def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [html.H3('Machine Learning dashboard', style={'textAlign':'center'}),
                    html.Hr(),
                    html.Div([html.H1('Machine Learning Dashbord', style=font_s),
                       html.Div([''], style = {'height':15, 'width':1700, 'background-color':color}),
                       html.Div([html.Div([' '], style = {'width':15}),
                                 html.Div([html.Div([' '], style = {'height':20}),
                                           html.H2('Regression algorithms', style = font_s),
                                           html.H3('Choose a model:', style = font_s),
                                           dcc.Dropdown(['Linear Regression', 'KNN Regression'],
                                                        'Linear Regression',
                                                        id = 'Model',
                                                        style={'font-family' : 'bahnschrift',
                                                               'width':370, 
                                                               'color': 'black', 
                                                               'background-color':'lightgray'}),
                                           html.H4('Additional parameters:', style = font_s),
                                           html.Div([html.B('   K=', style = {'font-family' : 'bahnschrift','width':370}),
                                                     daq.NumericInput(min=1,
                                                                      max=30,
                                                                      value=3,
                                                                      style = {'font-family' : 'bahnschrift'},
                                                                      id='K')], 
                                                    style={'display':'flex', 'width':370}),
                                           html.Div([html.B('   YEAR=', style = {'font-family' : 'bahnschrift','width':370}),
                                                     daq.NumericInput(min=2012,
                                                                      max=2018,
                                                                      value=2012,
                                                                      style = {'font-family' : 'bahnschrift'},
                                                                      id='YEAR')], 
                                                    style={'display':'flex', 'width':370}),
                                           html.H5('Metrics:', style = font_s),
                                           dash_table.DataTable(id= 'metrics_table', 
                                                                style_header={'backgroundColor': color, 'color':'lightgray','fontWeight': 'bold'},
                                                                style_cell={'textAlign': 'center', 'backgroundColor':'lightgray', 'color':'black'},
                                                                style_table={'width':370}, cell_selectable = False, 
                                                                style_as_list_view=True)]),
                                 html.Div([' '], style = {'width':15}),
                                 html.Div([' '], style = {'width':20,'background-color':color}),
                                 html.Div([' '], style = {'width':15}),
                                 html.Div([html.Div([''], style = {'height':15}),
                                           html.H3('Crop yield predictions', style = font_s),
                                           dcc.Graph(id="Yield_Pred", style = {'width':1100, 'height' : 350}),
                                           html.Div([''], style = {'height':15}),
                                           html.H3('Error estimations', style = font_s),
                                           dcc.Graph(id="Error", style = {'width':1100, 'height' : 350})],
                                         )],
                                style={'display':'flex', 'width':1700, 'height':900, 'overflow':'auto'}),
], style = {'overflow':'auto', 'height':1000})
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])

@callback(
    [Output('metrics_table', 'data'),Output('K', 'disabled'), Output('Yield_Pred', 'figure'), Output('Error','figure')],
    [Input('Model','value'),Input('K','value'), Input('YEAR','value')]
)
def update_metrics_n_map(model, K, year):
    
    if model == 'Linear Regression':
        K_not_needed = True
        model, y_pred = fit_regression('LR', X_train, X_test, y_train, y_test)
        df, df_e = get_error_n_predicted_GeoJSON(nuts2, 'LR', year)
        
    elif model == 'KNN Regression':
        K_not_needed = False
        model, y_pred = fit_regression('KNN', X_train, X_test, y_train, y_test, K)
        df, df_e = get_error_n_predicted_GeoJSON(nuts2, 'KNN', year, K)

    fig = px.choropleth_mapbox(df, 
                               geojson=df.geometry, 
                               locations = df.index,
                               color='est_crop_yield',
                               color_continuous_scale="greens",
                               range_color=(35, 55),
                               mapbox_style="carto-positron",
                               hover_data = ['NAME_LATN','est_crop_yield'],
                               zoom=5.8, center = {"lat": 52.05, "lon": 5.67}
                              )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        
    fig_e = px.choropleth_mapbox(df_e, 
                               geojson=df_e.geometry, 
                               locations = df_e.index,
                               color='Error',
                               color_continuous_scale="RdBu_r",
                               range_color=(-12, 12),
                               mapbox_style="carto-positron",
                               hover_data = ['NAME_LATN','Error'],
                               zoom=5.8, center = {"lat": 52.05, "lon": 5.67}
                              )
    fig_e.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    return get_metrics(y_test,y_pred), K_not_needed, fig, fig_e


