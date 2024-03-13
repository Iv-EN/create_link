import random

from sqlalchemy.exc import IntegrityError

from . import db
from .constants import (ALLOWED_CHARS, AUTO_LINK_LENGTH,
                        SHORT_ALREADY_EXISTS)
from .models import URLMap
from .validators import symbols_validation


def get_urls_for_form(form):
    """Проверяет данные полученные из формы."""
    original = form.original_link.data
    short = form.custom_id.data
    try:
        symbols_validation(short)
    except Exception as e:
        return original, short, e
    if not short:
        return original, get_unique_short_id(), None
    if short_url_exist(short):
        return original, short, SHORT_ALREADY_EXISTS
    return original, short, None


def get_unique_short_id() -> str:
    """Генерерует короткую ссылку из случайных символов."""
    short_link = ''.join(
        random.sample(ALLOWED_CHARS, AUTO_LINK_LENGTH)
    )
    if URLMap.query.filter_by(short=short_link).first():
        short_link = get_unique_short_id()
    return short_link


def short_url_exist(short_url):
    """Проверка существования короткой ссылки в базе данных."""
    return bool(URLMap.query.filter_by(short=short_url).first())


def add_url_map(original, short):
    """Сохраняет данные в БД."""
    url_map = URLMap(
        original=original,
        short=short
    )
    db.session.add(url_map)
    try:
        db.session.commit()
    except IntegrityError:
        return False
    return True