"""Модуль для настройки создания веб-приложения с указанным параметрами."""

import logging

from flask import Flask
from sqlalchemy.orm import scoped_session, sessionmaker

import config
from web_app.views import bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.context_processor(year)
    Base.metadata.create_all(bind=sync_engine)
    app.db_session = scoped_session(
        sessionmaker(
            bind=sync_engine,
            autocommit=False,
            autoflush=False
        )
    )

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        app.db_session.remove()

    app.register_blueprint(bp)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    logging.getLogger().addHandler(stream_handler)
    logging.getLogger().setLevel(logging.INFO)
    return app
