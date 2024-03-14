from flask import flash, redirect, render_template

from . import app
from .form import YacutForm
from .models import URLMap
from .utils import add_url_map, get_urls_for_form


@app.route('/', methods=['GET', 'POST', ])
def index_view():
    """Главная страница генерации коротких ссылок."""
    form = YacutForm()
    if form.validate_on_submit():
        original, short_link, error_message = get_urls_for_form(form)
        if error_message is not None:
            flash(error_message)
            return render_template('index.html', form=form)
        if not add_url_map(original, short_link):
            flash('Не удалось создать ссылку.')
            return render_template('index.html', form=form)
        flash('Ваша короткая ссылка готова:')
        flash(short_link)
    return render_template('index.html', form=form)


@app.route('/<short_url>', methods=('GET',))
def redirect_view(short_url):
    """Переадресация на исходный адрес."""
    original_url = URLMap.query.filter_by(short=short_url).first_or_404()
    return redirect(original_url.original)
