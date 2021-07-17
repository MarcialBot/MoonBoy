import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd


def init_dashboard(server):
# Initializes the dashboard view which displays all components
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix="/dashboard/",
    )


