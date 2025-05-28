"""Модуль для настройки тестирования веб-приложения."""

from unittest.mock import patch

from app.utils import search_cities


def test_search_cities():
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {
            "results": [{"name": "Test", "country": "RU"}]
        }
        cities = search_cities("test")
        assert len(cities) > 0
