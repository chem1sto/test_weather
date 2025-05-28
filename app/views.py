"""Модуль для настройки view-функций веб-приложения."""

import logging

from flask import Blueprint, jsonify, render_template, request, session

from app.utils import get_weather, search_cities
from config import MAIN_PAGE

logger = logging.getLogger(__name__)

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    """View-функция для обработки данных и рендеринга главной страницы."""
    weather_data = None
    if "history" not in session:
        session["history"] = []
    city = request.form.get("city") or session.get("last_city")
    session["history"].append(city)
    session.modified = True
    logger.info(f"В сессию добавлен новый город: {city}")
    if city:
        weather_data = get_weather(city)
        if weather_data:
            session["last_city"] = city
    logger.info(f"Загружена основная страница. Данные сессии: {session}")
    return render_template(MAIN_PAGE, weather=weather_data, city=city)


@main.route("/api/cities", methods=["GET"])
def city_autocomplete():
    """View-функция для автозаполнения городов в поиске."""
    query = request.args.get("q", "").strip()
    if len(query) < 2:
        return jsonify([])
    cities = search_cities(query)
    return jsonify(cities[:10])
