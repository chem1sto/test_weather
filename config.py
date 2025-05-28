"""Модуль для настройки веб-приложения."""

from app.constants import (
    FLASK_DEBUG,
    FLASK_DEFAULT_WEB_APP,
    FLASK_RUN_PORT,
    FLASK_SECRET_KEY,
)

ERROR_PAGE_404 = "404.html"
ERROR_PAGE_505 = "505.html"
MAIN_PAGE = "/pages/index.html"


class Config(object):
    FLASK_DEBUG = FLASK_DEBUG
    FLASK_RUN_PORT = FLASK_RUN_PORT
    SECRET_KEY = FLASK_SECRET_KEY
    FLASK_DEFAULT_WEB_APP = FLASK_DEFAULT_WEB_APP
