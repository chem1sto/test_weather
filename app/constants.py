"""Модуль для настройки переменных."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent.parent
ERROR_PAGE_404 = "/errors/404.html"
ERROR_PAGE_500 = "/errors/500.html"
FLASK_DEBUG = os.getenv("FLASK_DEBUG", False)
FLASK_RUN_PORT = os.getenv("FLASK_RUN_PORT", 5000)
FLASK_SECRET_KEY = os.getenv(
    "FLASK_SECRET_KEY",
    "192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf",
)
GEO_URL = "https://nominatim.openstreetmap.org/search"
GEO_URL_HEADERS = {"User-Agent": "test_weather/1.0 (vladvasiliev52@gmail.com)"}
GEO_RESPONSE_TIMEOUT = 5
MAIN_PAGE = "/pages/index.html"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
WEATHER_RESPONSE_TIMEOUT = 5
