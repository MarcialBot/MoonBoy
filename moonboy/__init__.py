from flask import Flask
from flask_assets import Environment


def init_app():
# Initializes instance of the application and creates dashboard instance
    app = Flask(__name__)
    assets = Environment()
    assets.init_app(app)

    with app.app_context():

        from . import routes
        from .dashboard import init_dashboard

        app = init_dashboard(app)

        return app

