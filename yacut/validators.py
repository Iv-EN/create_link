from .constants import ALLOWED_CHARS, INVALID_NAME
from .error_handlers import InvalidAPIUsage


def len_validation(link, exception=InvalidAPIUsage(INVALID_NAME), max=16, min=1):
    """Проверка длины созданной пользователем ссылки."""
    if min <= len(link) <= max:
        return None
    raise exception


def symbols_validation(link, exception=InvalidAPIUsage(INVALID_NAME)):
    """Проверка изпользованных в ссылке символов."""
    if isinstance(link, str) and all((symbol in ALLOWED_CHARS) for symbol in link):
        return None
    raise exception