from flask import Flask

def create_app():
    setup_logs()
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    setup_models(app)
    setup_controllers(app)

    return app

def setup_models(app):
    from .api import models
    models.init_app(app)

def setup_controllers(app):
    from .web import controllers
    controllers.init_app(app)

def setup_logs():
    from logging.config import dictConfig

    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })
