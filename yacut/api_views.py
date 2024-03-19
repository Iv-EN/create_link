from http import HTTPStatus

from flask import jsonify, request, url_for

from . import app, constants
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import add_url_map, get_unique_short_id, short_url_exist
from .validators import len_validation, symbols_validation


@app.route('/api/id/', methods=['POST'])
def create_link():
    """Обрабатывает запрос на создание короткой ссылки."""
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(constants.NO_DATA)
    original = data.get(constants.API_REQUEST_FIELDS.original)
    if original is None:
        raise InvalidAPIUsage(constants.NO_REQUIRED_FIELD)
    short = data.get(constants.API_REQUEST_FIELDS.short)
    if short:
        len_validation(
            short,
            InvalidAPIUsage(constants.INVALID_NAME),
            max=constants.USER_LINK_LENGHT
        )
        symbols_validation(short, InvalidAPIUsage(constants.INVALID_NAME))
        if short_url_exist(short):
            raise InvalidAPIUsage(constants.SHORT_ALREADY_EXISTS)
    else:
        short = get_unique_short_id()
    add_url_map(original, short)
    response_dict = {
        constants.API_RESPONSE_FIELDS.short: url_for(
            'redirect_view', short_url=short, _external=True
        ),
        constants.API_RESPONSE_FIELDS.original: original
    }

    return jsonify(response_dict), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original_url(short_id):
    """Получает оригинальную ссылку по короткой."""
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        raise InvalidAPIUsage(constants.ID_NOT_FOUND, HTTPStatus.NOT_FOUND)
    response_dict = {
        constants.API_RESPONSE_FIELDS.original: url_map.original
    }
    return response_dict, HTTPStatus.OK
