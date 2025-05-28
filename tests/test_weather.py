"""Модуль для настройки тестирования веб-приложения."""


def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    response = client.post("/", data={"city": "Moscow"})
    assert response.status_code == 200
    assert b"Moscow" in response.data
    with client.session_transaction() as session:
        assert "last_city" in session
        assert "history" in session
        assert "Moscow" in session["history"]


def test_clear_history(client):
    with client.session_transaction() as session:
        session["history"] = ["Moscow", "London"]
    response = client.get("/clear_history")
    assert response.status_code == 302
    with client.session_transaction() as session:
        assert "history" not in session
