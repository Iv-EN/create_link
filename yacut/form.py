from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Optional

from .constants import INVALID_ORIGINAL_NAME, NO_REQUIRED_FIELD


class YacutForm(FlaskForm):
    """Форма создания ссылок."""

    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message=NO_REQUIRED_FIELD),
            URL(message=INVALID_ORIGINAL_NAME)
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
        ]
    )
    submit = SubmitField('Создать')