"""Модуль для настройки веб-приложения."""

from app.constants import FLASK_DEBUG, FLASK_RUN_PORT, FLASK_SECRET_KEY


class Config(object):
    FLASK_DEBUG = FLASK_DEBUG
    FLASK_RUN_PORT = FLASK_RUN_PORT
    SECRET_KEY = FLASK_SECRET_KEY
