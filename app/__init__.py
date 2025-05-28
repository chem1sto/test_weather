"""Модуль для настройки создания веб-приложения с указанным параметрами."""

import logging

from flask import Flask

from app.context_processors import year
from app.views import main
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    logging.getLogger().addHandler(stream_handler)
    logging.getLogger().setLevel(logging.INFO)
    app.debug = app.config["FLASK_DEBUG"]
    if app.debug:
        app.config["TEMPLATES_AUTO_RELOAD"] = True
        app.jinja_env.auto_reload = True
        logging.basicConfig(level=logging.DEBUG)
    app.context_processor(year)
    app.register_blueprint(main)
    return app
