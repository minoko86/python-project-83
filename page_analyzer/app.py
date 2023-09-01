import os
from flask import Flask, render_template, get_flashed_messages


from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/')
def get_index():
    messages = get_flashed_messages(with_categories=True)
    return render_template('base.html', messages=messages)


@app.route('/urls')
def get_index1():
    messages = get_flashed_messages(with_categories=True)
    return render_template('urls.html', messages=messages)
