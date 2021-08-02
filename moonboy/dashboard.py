
# DASHBOARD COMPONENT

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.subplots as subplot
import pandas as pd
from .templates.layout import html_layout
import ccxt
from datetime import datetime
import calendar
import dash_bootstrap_components as dbc
from .data.exchange import Exchange

# DEFAULTS
ticker_pair = ("ETH/USDT")
exchange_name = ("coinbasepro")
timeframe = ("1m")

# VARIABLES
exchange = Exchange(exchange_name).api
markets = exchange.load_markets()
ticker = exchange.fetch_ticker(ticker_pair)
ohlcv = exchange.fetch_ohlcv(ticker_pair,timeframe)
exchanges = ccxt.exchanges


class Dashboard:

    def __init__(self, server):
        # Initializes the dashboard view which displays all components
        self.dash_app = dash.Dash(
            __name__,
            server=server,
            routes_pathname_prefix="/dashboard/",
            external_stylesheets=[dbc.themes.MINTY]
        )

    # VIEWS
    # Initializes other components
    # - Add calls to exchange class inits
    # - Make dashboard dashboard component based
    def create_layout(self):

        self.dash_app.layout=html.Div(
            children=[
                dbc.Row(children=[
                    dbc.Col(
                        html.Div(
                            dcc.Dropdown(
                                id='exchanges_dropdown',
                                options=[{'label': i.title(), 'value': i} for i in exchanges],
                                value='coinbasepro'
                            ),
                            style={"width":"15%"},
                        )),
                    dbc.Col(
                        html.Div(
                            dcc.Dropdown(
                                id='markets_dropdown',
                                options=[{'label': j, 'value': j} for j in markets],
                                value='ETH/USDT'
                            ),
                        style={"width": "15%"},
                    )),
                ]),
                dcc.Graph(id='candlestick_graph'),
                dcc.Interval(
                    id='interval-component',
                    interval=1*1000,
                    n_intervals=0
                )
            ],
        )

        return self.dash_app.server

        @dash_app.callback(
            Output(component_id='candlestick_graph', component_property='figure'),
            Input(component_id='exchanges_dropdown', component_propery='value')
        )
        def update_dash(input_value):

            # Figure out how to get to run for duration of dashboard instance

            df = pd.DataFrame(ohlcv, columns = ['Timeframe', 'Open', 'High', 'Low', 'Close', 'Volume'])
            df['Timeframe'] = [datetime.fromtimestamp(float(time)/1000) for time in df['Timeframe']]

            exchange_name = input_value

            # CANDLESTICK LAYOUT
            candle_layout = dict(
                title = ticker_pair,
                xaxis = go.layout.XAxis(title=go.layout.xaxis.Title(text='Time')),
                yaxis = go.layout.YAxis(title=go.layout.yaxis.Title(text="Price"))
            )

            candlesticks = [go.Candlestick(x=df['Timeframe'],
                                           open=df['Open'],
                                           high=df['High'],
                                           low=df['Low'],
                                           close=df['Close'])]

            candlesticks.update_layout(transition_duration=500)

            candle_fig = go.Figure(data=candlesticks,layout=candle_layout)

            figure=candle_fig
            return figure


