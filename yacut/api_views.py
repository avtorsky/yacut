from http import HTTPStatus as status
from re import match

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id

ERROR_SHORT_URL = 'Указано недопустимое имя для короткой ссылки'
ERROR_URL = 'Недопустимый URL'
MISSING_PAYLOAD = 'Отсутствует тело запроса'
NOT_FOUND_ID = 'Указанный id не найден'
REGEXP_SHORT_URL = r'^[A-Za-z0-9_]{1,16}$'
REGEXP_URL = r'^[a-z]+://[^\/\?:]+(:[0-9]+)?(\/.*?)?(\?.*)?$'
REQUIRED_URL = '"url" является обязательным полем!'
RESERVED_ID = 'Имя "{}" уже занято.'


@app.route('/api/id/<string:short>/', methods=['GET'])
def url_redirect_api(short):
    redirect = URLMap.query.filter_by(short=short).first()
    if not redirect:
        raise InvalidAPIUsage(NOT_FOUND_ID, status.NOT_FOUND)
    return jsonify({'url': redirect.original})


@app.route('/api/id/', methods=['POST'])
def create_short_api():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(MISSING_PAYLOAD)
    if 'url' not in data:
        raise InvalidAPIUsage(REQUIRED_URL)
    if not match(REGEXP_URL, data['url']):
        raise InvalidAPIUsage(ERROR_URL)
    if not data.get('custom_id'):
        data['custom_id'] = get_unique_short_id()
    elif URLMap.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPIUsage(RESERVED_ID.format(data['custom_id']))
    elif not match(REGEXP_SHORT_URL, data['custom_id']):
        raise InvalidAPIUsage(ERROR_SHORT_URL)
    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), status.CREATED
