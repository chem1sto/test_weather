"""Модуль для настройки создания веб-приложения с указанным параметрами."""

import logging

from flask import Flask

from app.views import main
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(main)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    logging.getLogger().addHandler(stream_handler)
    logging.getLogger().setLevel(logging.INFO)
    return app
