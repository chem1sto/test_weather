"""Модуль для настройки создания веб-приложения с указанным параметрами."""

import logging

from flask import Flask

from app.context_processors import year
from app.views import main
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.context_processor(year)
    app.register_blueprint(main)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    logging.getLogger().addHandler(stream_handler)
    logging.getLogger().setLevel(logging.INFO)
    return app
