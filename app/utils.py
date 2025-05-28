"""Модуль для настройки вспомогательных функций для веб-приложения."""

import logging

import requests

from app.constants import (
    GEO_RESPONSE_TIMEOUT,
    GEO_URL,
    GEO_URL_HEADERS,
    WEATHER_RESPONSE_TIMEOUT,
    WEATHER_URL,
)

logger = logging.getLogger(__name__)


def get_weather(city_name):
    """Получение и обработка данных по погоде."""
    try:
        geo_response = requests.get(
            GEO_URL,
            params={
                "q": city_name,
                "format": "json",
                "addressdetails": 1,
                "limit": 1,
                "accept-language": "ru",
            },
            headers=GEO_URL_HEADERS,
            timeout=GEO_RESPONSE_TIMEOUT,
        )
        geo_response.raise_for_status()
        geo_data = geo_response.json()
        if not geo_data:
            logger.warning(f"Не был найден город {city_name}")
            return {
                "error": (
                    f"Город '{city_name}' не найден. Проверьте написание "
                    f"или попробуйте другой город."
                )
            }
        location = geo_data[0]
        weather_params = {
            "latitude": location["lat"],
            "longitude": location["lon"],
            "current_weather": "true",
            "hourly": "temperature_2m",
            "timezone": "auto",
        }
        weather_response = requests.get(
            WEATHER_URL,
            params=weather_params,
            timeout=WEATHER_RESPONSE_TIMEOUT,
        )
        weather_response.raise_for_status()
        return weather_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе данных: {e}")
        return None
    except (KeyError, IndexError) as e:
        print(f"Ошибка обработки данных: {e}")
        return None


def search_cities(query):
    """Поиск городов для автозаполнения поисковой строки."""
    try:
        response = requests.get(
            GEO_URL,
            params={
                "q": query,
                "format": "json",
                "addressdetails": 1,
                "limit": 10,
                "accept-language": "ru",
            },
            headers=GEO_URL_HEADERS,
            timeout=GEO_RESPONSE_TIMEOUT,
        )
        response.raise_for_status()
        cities_data = response.json()
        return [
            {"name": item["display_name"].split(",")[0]}
            for item in cities_data
        ]
    except Exception as e:
        print(f"Ошибка поиска: {e}")
        return []
