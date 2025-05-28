"""Модуль для настройки api-эндпоинтов веб-приложения."""

import logging

from flask import Blueprint, jsonify, request

from app.utils import search_cities
from app.views import city_stats

api_bp = Blueprint("api_bp", __name__)

logger = logging.getLogger(__name__)


@api_bp.route("/api/cities/", methods=["GET"])
def city_autocomplete():
    """Автозаполнение названия городов в форме поиска."""
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
    return jsonify(unique_cities)


@api_bp.route("/api/city_stats/", methods=["GET"])
def get_city_stats():
    """Возвращает статистику запросов городов."""
    logger.info("Получен запрос на получение статистики запросов городов")
    return jsonify(
        dict(sorted(city_stats.items(), key=lambda x: x[1], reverse=True))
    )
