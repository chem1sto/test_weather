"""Модуль для настройки переменных."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent.parent
FLASK_DEBUG = os.getenv("FLASK_DEBUG", False)
FLASK_RUN_PORT = os.getenv("FLASK_RUN_PORT", 5000)
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "123456")
FLASK_DEFAULT_WEB_APP = os.getenv("DEFAULT_WEB_APP", "web_app")
GEO_URL = os.getenv(
    "GEO_URL",
    "https://geocoding-api.open-meteo.com/v1/search?name={city_name}",
)
WEATHER_URL = (
    "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude="
    "{lon}&current_weather=true"
)
