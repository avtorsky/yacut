from random import choices
from string import ascii_letters, digits

from flask import flash, redirect, render_template, request

from . import app, db
from .forms import YacutForm
from .models import URLMap

READY_SHORT_URL = (
    'Ваша новая ссылка готова: '
    '<a href="{short_url}">{short_url}</a>'
)


def get_unique_short_id():
    while True:
        short_id = ''.join(choices(ascii_letters + digits, k=6))
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = YacutForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = get_unique_short_id()
        elif URLMap.query.filter_by(short=custom_id).first():
            form.custom_id.errors = [f'Имя {custom_id} уже занято!']
            return render_template('main.html', form=form)
        url_map = URLMap(
            original=form.original_link.data,
            short=custom_id,
        )
        db.session.add(url_map)
        db.session.commit()
        flash(
            READY_SHORT_URL.format(short_url=f'{request.base_url}{custom_id}')
        )
    return render_template('main.html', form=form)


@app.route('/<string:short>', methods=['GET'])
def url_redirect(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )
