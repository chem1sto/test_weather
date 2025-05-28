"""Модуль для настройки кастомных перехватчиков ошибок."""

from http import HTTPStatus

from flask import render_template

from app.constants import ERROR_PAGE_404, ERROR_PAGE_500


def page_not_found(error):
    return render_template(ERROR_PAGE_404), HTTPStatus.NOT_FOUND


def internal_error(error):
    return render_template(ERROR_PAGE_500), HTTPStatus.INTERNAL_SERVER_ERROR
