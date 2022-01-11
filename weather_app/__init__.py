import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',

    )
    if test_config is None:
        app.config.from_pyfile('config.py')

    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import forecast
    app.register_blueprint(forecast.forecast)
    app.add_url_rule('/forecast',endpoint='forecast_location')
    from . import home
    app.register_blueprint(home.home)
    app.add_url_rule('/', endpoint='index')


    
    return app
        