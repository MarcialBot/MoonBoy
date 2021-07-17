import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import ccxt

default_exchange = 'coinbasepro'
exchange_df = pd.DataFrame(ccxt.exchanges)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
available_exchanges = exchange_df[0].unique()
exchange = getattr (ccxt, default_exchange)
df = pd.DataFrame(eval(exchange))
if exchange.has['fetchOHLCV'] == True:
    timeframes = pd.Series(exchange.timeframes)




app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


app.logger.info('%s exchange', timeframes)
app.layout = html.Div([
    dcc.Dropdown(
        id='exchange-dropdown',
        options=[
            {'label': i, 'value': i} for i in available_exchanges
        ],
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
