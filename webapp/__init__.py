from flask import Flask, render_template, request, flash, url_for, redirect

from webapp.forms import ProfileForm, SearchForm
from webapp.model import db, Worker, Properties
from webapp.new_worker import add_new_worker
from webapp.search_worker import search_worker


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

        worker = Worker.query.all()

        return render_template('patronazh.html', worker=worker)

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

    @app.route('/worker')
    def worker():
        form = ProfileForm()
        return render_template('worker_profile.html', form=form)

    @app.route('/add_worker', methods=['POST'])
    def add_worker():
        all_args = request.form.to_dict()
        all_args.pop('csrf_token')
        all_args.get('')

        properties = request.form.getlist("properties")

        client_age = request.form.getlist("client-age")
        client_age = ', '.join(client_age)

        if Worker.query.filter(Worker.email == all_args['email']).count():
            flash('Такой пользователь уже есть')
            return redirect(url_for('worker'))
        else:
            add_new_worker(all_args, properties, client_age)

        flash('Пользователь успешно добавлен!')
        return redirect(url_for('patronage'))

    @app.route('/search_results', methods=['POST'])
    def search_results():
        form = SearchForm()

        options = request.form.getlist("search_request")
        gender = request.form.getlist("gender")
        agefrom = request.form.get('agefrom')
        ageto = request.form.get('ageto')
        pricefrom = request.form.get('pricefrom')
        priceto = request.form.get('priceto')
        shedule = request.form.getlist('shedule')

        worker = search_worker(options, priceto, pricefrom, agefrom, ageto, gender, shedule)

        return render_template('search_results.html', worker=worker)

    return app
