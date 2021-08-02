from flask import Flask
from flask_assets import Environment


def init_app():
# Initializes instance of the application and creates dashboard instance
    app = Flask(__name__)
    assets = Environment()
    assets.init_app(app)

    with app.app_context():

        #Import core Flask App
        from . import routes

        #Import Dash App
        from .dashboard import Dashboard
        app = Dashboard(app)
        app = app.create_layout()

        return app

