"""Модуль для настройки точки входа в веб-приложения."""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(
        host=app.config.get("HOST", "0.0.0.0"),
        port=app.config.get("PORT", 5000),
        debug=app.config.get("FLASK_DEBUG", True),
    )
