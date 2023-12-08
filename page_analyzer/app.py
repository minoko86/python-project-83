import logging
import os
from urllib.parse import urlparse

# import psycopg2
from dotenv import load_dotenv
from flask import (Flask, abort, flash, redirect, render_template, request,
                   url_for)

from page_analyzer import db, html
from page_analyzer.validator import validate
from page_analyzer.url import get_response

load_dotenv()
# DATABASE_URL = os.getenv('DATABASE_URL')
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

# conn = psycopg2.connect(DATABASE_URL)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    logging.exception(str(e))
    return render_template('500.html'), 500


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/urls')
def urls_list():
    # with conn:
    urls = db.get_all_urls()
    url_checks = {
        item.url_id: item for item in db.get_last_url_checks()
    }
    return render_template(
        '/urls.html',
        urls=urls,
        url_checks=url_checks
    )


@app.post('/urls')
def url_add():
    url_name = request.form.get('url')
    errors = validate(url_name)
    if errors:
        for error in errors:
            flash(error, 'error')
        return render_template(
            'index.html',
        ), 422
    url_parsed = urlparse(url_name)
    url_name = f'{url_parsed.scheme}://{url_parsed.netloc}'
    # with conn:
    url_to_check = db.get_url_by_name(url_name)
    if url_to_check:
        flash('Страница уже существует', 'info')
        return redirect(url_for('url_info', id=url_to_check[0]))
    url_id = db.create_url(url_name)
    flash('Страница успешно добавлена', 'success')
    return redirect(url_for('url_info', id=url_id))


@app.get('/urls/<id>')
def url_info(id):
    # with conn:
    url = db.get_url_by_id(id)
    if not url:
        abort(404)
    url_checks = db.get_checks_by_url_id(id)
    return render_template(
        'urls_id.html',
        url=url,
        checks=url_checks
    )


@app.post('/urls/<id>/checks')
def url_check(id):
    # with conn:
    url = db.get_url_by_id(id)
    response = get_response(url)
    if not url:
        abort(404)
    if not response:
        flash('Произошла ошибка при проверке', 'error')
        return redirect(url_for('url_info', id=id))
    status_code = response.status_code
    h1, title, description = html.get_seo_data(response.text)
    db.create_check(id, status_code, h1, title, description)
    flash('Страница успешно проверена', 'success')
    return redirect(url_for('url_info', id=id))
