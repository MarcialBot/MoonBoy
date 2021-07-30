
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

def init_dashboard(server):
    # Initializes the dashboard view which displays all components
    dash_app = dash.Dash(
        __name__,
        server=server,
        routes_pathname_prefix="/dashboard/",
        external_stylesheets=[dbc.themes.MINTY]
    )

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

    df = pd.DataFrame(ohlcv, columns = ['Timeframe', 'Open', 'High', 'Low', 'Close', 'Volume'])
    df['Timeframe'] = [datetime.fromtimestamp(float(time)/1000) for time in df['Timeframe']]

    
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

    candle_fig = go.Figure(data=candlesticks,layout=candle_layout)

    # VIEWS
    # Initializes other components
    # - Add calls to exchange class inits
    dash_app.layout=html.Div(
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
            dcc.Graph(
                id='candlestick_graph',
                figure=candle_fig,
            ),
        ],
    )



    return dash_app.server

