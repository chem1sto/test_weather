"""Модуль для настройки вспомогательных функций для веб-приложения."""

import requests

from app.constants import GEO_URL, WEATHER_URL


def get_weather(city_name):
    """Получение и обработка данных по погоде."""
    geo_response = requests.get(GEO_URL.format(city_name=city_name)).json()
    if not geo_response.get("results"):
        return None
    location = geo_response["results"][0]
    lat, lon = location["latitude"], location["longitude"]
    return requests.get(WEATHER_URL.format(lat=lat, lon=lon)).json()


def search_cities(query):
    """Поиск городов для автозаполнения поисковой строки."""
    params = {"name": query, "count": 5, "language": "ru"}
    response = requests.get(GEO_URL, params=params)
    return response.json().get("results", [])
