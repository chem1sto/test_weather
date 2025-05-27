"""Модуль для настройки view-функций веб-приложения."""

import requests

from app.constants import GEO_URL, WEATHER_URL


def get_weather(city_name):
    """View-функция для получения и обработки данных по погоде."""
    geo_response = requests.get(GEO_URL.format(city_name=city_name)).json()
    if not geo_response.get("results"):
        return None
    location = geo_response["results"][0]
    lat, lon = location["latitude"], location["longitude"]
    return requests.get(WEATHER_URL.format(lat=lat, lon=lon)).json()
