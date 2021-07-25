# Routes for parent Flask App

from flask import render_template
from flask import current_app as app

@app.route('/')
def home():
    #Landing Page

    return render_template(
        'index.jinja2',
        title='MoonBoy',
        description='Trading bot for the moon boys & girls.',
        template='home-template',
        body="Moon boy is the hero of all traders."
    )
