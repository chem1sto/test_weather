"""Модуль для настройки view-функций веб-приложения."""

import logging

from flask import Blueprint, render_template, request, session

from app.utils import get_weather

logger = logging.getLogger(__name__)

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    city = request.form.get("city") or session.get("last_city")
    if city:
        weather_data = get_weather(city)
        if weather_data:
            session["last_city"] = city
    return render_template("index.html", weather=weather_data, city=city)
