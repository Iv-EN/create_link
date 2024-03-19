from .constants import (ALLOWED_CHARS, INVALID_NAME, USER_LINK_LENGHT,
                        USER_LINK_LENGHT_MIN)
from .error_handlers import InvalidAPIUsage


def len_validation(
        link,
        exception=InvalidAPIUsage(INVALID_NAME),
        max=USER_LINK_LENGHT, min=USER_LINK_LENGHT_MIN
):
    """Проверка длины созданной пользователем ссылки."""
    if min <= len(link) <= max:
        return None
    raise exception


def symbols_validation(link, exception=InvalidAPIUsage(INVALID_NAME)):
    """Проверка изпользованных в ссылке символов."""
    if isinstance(link, str) and all((symbol in ALLOWED_CHARS) for symbol in link):
        return None
    raise exception