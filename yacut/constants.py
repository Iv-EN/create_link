import string
from collections import namedtuple

URL_MAP_FIELDS = namedtuple('Fields', 'id original short timestamp')
"""Именованный кортеж с именами полей из модели URLMap."""
API_REQUEST_FIELDS = URL_MAP_FIELDS(None, 'url', 'custom_id', None)
"""Связывает поля API-запроса с полями URLMap."""
API_RESPONSE_FIELDS = URL_MAP_FIELDS(None, 'url', 'short_link', None)
"""Связывает поля API-ответа с полями URLMap."""

ALLOWED_CHARS = string.ascii_letters + string.digits
"""Допустимые символы для короткой ссылки."""
AUTO_LINK_LENGTH = 6
"""Максимальная длина ссылки по умолчанию."""
USER_LINK_LENGHT = 16
"""Максимальная длина пользовательского варианта ссылки."""
ORIGINAL_LINK_LENGHT = 256
"""Максимальная длина оригинальной ссылки."""

NO_DATA = 'Отсутствует тело запроса'
"""Отсутствует тело запроса."""
NO_REQUIRED_FIELD = '\"url\" является обязательным полем!'
"""Не заполнено поле 'url'."""
SHORT_ALREADY_EXISTS = 'Предложенный вариант короткой ссылки уже существует.'
"""Короткая ссылка уже существует."""
INVALID_NAME = 'Указано недопустимое имя для короткой ссылки'
"""Указано недопустимое имя короткой ссылки."""
INVALID_ORIGINAL_NAME = 'Некорректная ссылка'
"""Указана некорректная ссылка."""
ID_NOT_FOUND = 'Указанный id не найден'
"""Указанный id не найден."""
