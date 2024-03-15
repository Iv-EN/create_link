import random

from sqlalchemy import exists
from sqlalchemy.exc import IntegrityError
from typing import Tuple, Union

from . import db
from .constants import (ALLOWED_CHARS, AUTO_LINK_LENGTH, INVALID_NAME,
                        SHORT_ALREADY_EXISTS, USER_LINK_LENGHT)
from .form import YacutForm
from .models import URLMap
from .validators import len_validation, symbols_validation


def get_urls_for_form(form: YacutForm) -> Tuple[str, str, Union[str, None]]:
    """Проверяет данные полученные из формы."""
    original = form.original_link.data
    short = form.custom_id.data
    if not short:
        return original, get_unique_short_id(), None
    if short_url_exist(short):
        return original, short, SHORT_ALREADY_EXISTS
    try:
        len_validation(short, max=USER_LINK_LENGHT)
        symbols_validation(short)
    except Exception:
        return original, short, INVALID_NAME
    return original, short, None


def get_unique_short_id() -> str:
    """Генерерует короткую ссылку из случайных символов."""
    while True:
        short_link = ''.join(
            random.sample(ALLOWED_CHARS, AUTO_LINK_LENGTH)
        )
        if not URLMap.query.filter_by(short=short_link).first():
            break
    return short_link


def short_url_exist(short_url: str) -> bool:
    """Проверка существования короткой ссылки в базе данных."""
    return db.session.query(exists().where(URLMap.short == short_url)).scalar()


def add_url_map(original: str, short: str) -> bool:
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