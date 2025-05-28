"""Модуль для настройки тестирования api-эндпоинтов веб-приложения."""

from unittest.mock import patch

from app.views import city_stats


@patch("app.views.search_cities")
def test_city_autocomplete(mock_search, client):
    mock_search.return_value = [{"name": "Moscow", "country": "RU"}]
    response = client.get("/api/cities/?q=a")
    assert response.json == []
    response = client.get("/api/cities/?q=mos")
    assert response.status_code == 200
    assert response.json == [{"name": "Moscow", "country": "RU"}]


def test_city_stats(client):
    city_stats["Moscow"] = 5
    city_stats["London"] = 3
    response = client.get("/api/city_stats/")
    assert response.status_code == 200
    assert response.json == {"Moscow": 5, "London": 3}
