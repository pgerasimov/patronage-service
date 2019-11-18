from flask import Flask, render_template

from webapp.forms import ProfileForm
from webapp.model import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/")
    def index():
        title = 'Патронаж Сервис'

        return render_template('index.html', page_title=title)

    @app.route('/patronage')
    def patronage():
        return render_template('patronazh.html')

    @app.route('/hospital')
    def hospital():
        return render_template('stacionar.html')

    @app.route('/patronage_item')
    def patronage_item():
        return render_template('patronazh_item.html')

    @app.route('/hospital_item')
    def hospital_item():
        return render_template('stacionar_item.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/send_form')
    def send_form():
        return 'ok'

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/login_process')
    def login_process():
        return 'ok'

    @app.route('/anketa')
    def anketa():
        form = ProfileForm()
        return render_template('anketa.html', form=form)

    return app
