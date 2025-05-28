"""Модуль для настройки интеграционных тестов веб-приложения."""

from unittest.mock import patch


def test_session_management(client):
    client.get("/")
    with client.session_transaction() as session:
        assert "history" in session
        assert session["history"] == []
    client.post("/", data={"city": "Berlin"})
    with client.session_transaction() as session:
        assert "Berlin" in session["history"]


def test_invalid_city(client):
    with patch("app.views.get_weather") as mock_get:
        mock_get.return_value = None
        response = client.post("/", data={"city": "InvalidCity"})
        assert response.status_code == 200
        assert b"InvalidCity" in response.data


def test_template_rendering(client):
    response = client.get("/")
    assert b"<form" in response.data
    assert "погоду".encode("utf-8") in response.data
