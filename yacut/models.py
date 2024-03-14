from datetime import datetime


from yacut import db

from .constants import ORIGINAL_LINK_LENGHT, USER_LINK_LENGHT


class URLMap(db.Model):
    """Объект для связи оригинальной и короткой ссылок."""
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_LINK_LENGHT), index=True, nullable=False)
    short = db.Column(db.String(USER_LINK_LENGHT), index=True, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
