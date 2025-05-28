"""Модуль для настройки context processor."""

from datetime import datetime


def year():
    """Возвращает текущий год."""
    return dict(year=datetime.now().year)
