from flask import Flask, render_template, request

from webapp.forms import ProfileForm
from webapp.model import db, Worker


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

    @app.route('/worker')
    def worker():
        form = ProfileForm()
        return render_template('worker_profile.html', form=form)

    @app.route('/add_worker', methods=['POST'])
    def add_worker():
        properties_map = {'medical': 0, 'recomendations': 0, 'diabet': 0, 'insult': 0, 'alzheimer': 0,
                          'dcp': 0, 'bed': 0, 'oncology': 0, 'hygiene': 0, 'injections': 0, 'dropper': 0, 'lfk': 0,
                          'cooking': 0, 'buyfood': 0, 'cleaning': 0, 'walking': 0}

        all_args = request.form.to_dict()
        all_args.pop('csrf_token')

        properties = request.form.getlist("properties")

        client_age = request.form.getlist("client-age")
        client_age = ', '.join(client_age)

        for item in properties:
            if item in properties_map.keys():
                properties_map[item] = 1

        print(all_args)
        print(f'Возраст клиента - {client_age}')
        print(f"Опции чекбоксов - {properties_map}")

        new_worker = Worker(surname=all_args['surname'], name=all_args['name'], mname=all_args['mname'],
                            age=all_args['age'], bio=all_args['bio'], phone=all_args['phone'],
                            email=all_args['email'], pricefrom=all_args['pricefrom'], priceto=all_args['priceto'],
                            experience=all_args['experience'], shedule=all_args['shedule'], gender=all_args['sex'])
        db.session.add(new_worker)
        db.session.commit()

        return 'ok'

    return app
