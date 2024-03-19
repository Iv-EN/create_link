from http import HTTPStatus

from flask import jsonify, render_template

from . import app, db


class InvalidAPIUsage(Exception):
    """Обработчик ошибок энпоинтов /api/*."""

    def __init__(self, message, status_code=HTTPStatus.BAD_REQUEST) -> None:
        super().__init__()
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        """Формирует сообщение об ошибке в формате словаря."""
        return {"message": self.message}


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    """Обработка ошибок для API."""
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(error):
    """Обработка ошибки 404."""
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_error(error):
    """Обработка ошибки сервера 500."""
    db.session.rollback()
    return render_template('500.html'), HTTPStatus.INTERNAL_SERVER_ERROR