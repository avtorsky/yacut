from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

DESCRIPTION_SHORT_URL = 'Cвой вариант короткой ссылки'
DESCRIPTION_URL = 'Оригинальная ссылка'
REQUIRED_FIELD = 'Обязательное поле'
ERROR_URL = 'Недопустимый URL'
ERROR_SHORT_URL = 'Недопустимое имя для короткой ссылки'
ERROR_SHORT_URL_LEN = 'Короткая ссылка не может быть больше 16 символов'
REGEXP_SHORT_URL = r'^[A-Za-z0-9_]+$'


class YacutForm(FlaskForm):
    original_link = URLField(
        DESCRIPTION_URL,
        validators=[
            DataRequired(message=REQUIRED_FIELD),
            URL(require_tld=True, message=ERROR_URL),
        ],
    )
    custom_id = URLField(
        DESCRIPTION_SHORT_URL,
        validators=[
            Length(1, 16, message=ERROR_SHORT_URL_LEN),
            Optional(),
            Regexp(REGEXP_SHORT_URL, message=ERROR_SHORT_URL),
        ],
    )
    submit = SubmitField('Создать')
