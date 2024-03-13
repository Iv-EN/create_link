"""
Проверка данных при работе с API.
"""
from .constants import ALLOWED_CHARS, INVALID_NAME


def len_validation(link, exception, max, min=1):
    try:
        getattr(link, '__len__')
    except AttributeError:
        raise AttributeError
    if min <= len(link) <= max:
        return None
    raise exception


def symbols_validation(link, exception=INVALID_NAME):
    if isinstance(link, str) and all((symbol in ALLOWED_CHARS) for symbol in link):
        return None
    raise exception