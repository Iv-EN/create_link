from datetime import datetime

from flask import url_for

from yacut import db

from .constants import ORIGINAL_LINK_LENGHT, USER_LINK_LENGHT


class URLMap(db.Model):
    """Объект для связи оригинальной и короткой ссылок."""
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_LINK_LENGHT), index=True, nullable=False)
    short = db.Column(db.String(USER_LINK_LENGHT), index=True, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self) -> dict:
        """Сериализатор."""
        return dict(
            url=self.original,
            short_link=url_for(
                'redirect_view', custom_id=self.short, _external=True
            ),
        )

    def __repr__(self):
        """Строковое представление объекта URLMap."""
        return (
            f'id: {self.id}\n'
            f'оригинальная ссылка: {self.original}\n'
            f'короткая ссылка: {self.short}\n'
            f'дата создания: {self.timestamp}\n'
        )
