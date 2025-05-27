"""Модуль для настройки веб-приложения."""

from constants import (
    FLASK_DEBUG,
    FLASK_DEFAULT_WEB_APP,
    FLASK_RUN_PORT,
    FLASK_SECRET_KEY,
)

ERROR_PAGE_404 = "404.html"
ERROR_PAGE_505 = "505.html"
MAIN_PAGE = "/pages/index.html"
ROOM_PAGE = "/pages/room.html"
START_GAME_COUNTDOWN = "/pages/start_game_countdown.html"
WELCOME_TO_THE_NEW_GAME = "/pages/welcome_to_the_new_game.html"


class Config(object):
    FLASK_DEBUG = FLASK_DEBUG
    FLASK_RUN_PORT = FLASK_RUN_PORT
    SECRET_KEY = FLASK_SECRET_KEY
    FLASK_DEFAULT_WEB_APP = FLASK_DEFAULT_WEB_APP
