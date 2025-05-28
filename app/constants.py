"""Модуль для настройки переменных."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent.parent
FLASK_DEBUG = os.getenv("FLASK_DEBUG", True)
FLASK_RUN_PORT = os.getenv("FLASK_RUN_PORT", 5000)
FLASK_SECRET_KEY = os.getenv(
    "FLASK_SECRET_KEY",
    "192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf",
)
GEO_URL = os.getenv(
    "GEO_URL",
    "https://geocoding-api.open-meteo.com/v1/search?name={city_name}",
)
WEATHER_URL = (
    "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude="
    "{lon}&current_weather=true"
)
