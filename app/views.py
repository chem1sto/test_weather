"""Модуль для настройки view-функций веб-приложения."""

import logging

from flask import (
    Blueprint,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from app.utils import get_weather, search_cities
from config import MAIN_PAGE

logger = logging.getLogger(__name__)

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    """View-функция для обработки данных и рендеринга главной страницы."""
    weather_data = None
    city = request.form.get("city") or session.get("last_city")
    if "history" not in session:
        session["history"] = []
    if request.method == "POST" and city:
        normalized_city = city.strip().title()
        if normalized_city not in session["history"]:
            session["history"].append(normalized_city)
        session["last_city"] = normalized_city
        session.modified = True
        weather_data = get_weather(normalized_city)
    elif request.method == "GET" and "last_city" in session:
        city = session["last_city"]
        weather_data = get_weather(city)
    logger.info(f"Загружена основная страница. Данные сессии: {session}")
    return render_template(MAIN_PAGE, weather=weather_data, city=city.title())


@main.route("/clear_history")
def clear_history():
    if "history" in session:
        session.pop("history")
        session.modified = True
        logger.info(
            f"История запросов по городам очищена. Данные сессии: {session}"
        )
    return redirect(url_for("main.index"))


@main.route("/api/cities", methods=["GET"])
def city_autocomplete():
    """View-функция для автозаполнения городов в поиске."""
    query = request.args.get("q", "").strip()
    if len(query) < 2:
        return jsonify([])
    cities = search_cities(query)
    unique_cities = []
    seen = set()
    for city in cities:
        if city["name"] not in seen:
            seen.add(city["name"])
            unique_cities.append(city)
    return jsonify(unique_cities[:8])
