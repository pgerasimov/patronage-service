from flask import Flask, render_template, request, flash, url_for
from werkzeug.utils import redirect

from webapp.forms import ProfileForm
from webapp.model import db, Worker, Properties


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
        worker = Worker.query.filter_by(email='gerasimov8611@gmail.com').all()
        woker_prop = Properties.query.filter_by(worker_id='3').all()
        print(woker_prop)
        return render_template('about.html', worker=worker, prop = woker_prop)

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

        print(f"Опции чекбоксов - {properties_map}")

        if Worker.query.filter(Worker.email == all_args['email']).count():
            flash('Такой пользователь уже есть')
            return redirect(url_for('worker'))
        else:
            new_worker = Worker(surname=all_args['surname'], name=all_args['name'], mname=all_args['mname'],
                                age=all_args['age'], bio=all_args['bio'], phone=all_args['phone'],
                                email=all_args['email'], pricefrom=all_args['pricefrom'], priceto=all_args['priceto'],
                                experience=all_args['experience'], shedule=all_args['shedule'], gender=all_args['sex'])

            db.session.add(new_worker)
            db.session.commit()

            new_worker_properties = Properties(medical=properties_map['medical'],
                                               recomendations=properties_map['recomendations'],
                                               diabet=properties_map['diabet'], insult=properties_map['insult'],
                                               alzheimer=properties_map['alzheimer'], dcp=properties_map['dcp'],
                                               bed=properties_map['bed'],
                                               oncology=properties_map['oncology'], hygiene=properties_map['hygiene'],
                                               injections=properties_map['injections'],
                                               dropper=properties_map['dropper'],
                                               lfk=properties_map['lfk'], cooking=properties_map['cooking'],
                                               buyfood=properties_map['buyfood'],
                                               cleaning=properties_map['cleaning'], walking=properties_map['walking'],
                                               patient_age=client_age, worker_id=new_worker.id)
            db.session.add(new_worker_properties)
            db.session.commit()

            flash('Пользователь успешно добавлен!')
            return redirect(url_for('index'))

    return app
