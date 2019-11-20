from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(120))
    last_login = db.Column(db.DateTime, default=datetime.datetime.now)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.email)


class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    surname = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(200), nullable = True)
    email = db.Column(db.String(200), nullable = False)
    photo = db.Column(db.String(200), nullable=True,
                      default='https://southatlanticpackaging.com/wp-content/uploads/2017/07/placeholder-person.gif')
    bio = db.Column(db.String(1000), nullable=True, default='Нет подробного описания')
    pricefrom = db.Column(db.Integer, nullable=True)
    priceto = db.Column(db.Integer, nullable=True)
    experience = db.Column(db.Integer, nullable=False)
    shedule = db.Column(db.Integer, nullable=True)
    medical = db.Column(db.Integer, nullable=True, default=0)



class Properties(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_age = db.Column(db.String(100), nullable=True, default=0)
    recomendations = db.Column(db.Integer, nullable=True, default=0)
    isphoto = db.Column(db.Integer, nullable=True, default=0)
    isrewiev = db.Column(db.Integer, nullable=True, default=0)
    diabet = db.Column(db.Integer, nullable=True, default=0)
    insult = db.Column(db.Integer, nullable=True, default=0)
    alzheimer = db.Column(db.Integer, nullable=True, default=0)
    dcp = db.Column(db.Integer, nullable=True, default=0)
    bed = db.Column(db.Integer, nullable=True, default=0)
    oncology = db.Column(db.Integer, nullable=True, default=0)
    hygiene = db.Column(db.Integer, nullable=True, default=0)
    injections = db.Column(db.Integer, nullable=True, default=0)
    dropper = db.Column(db.Integer, nullable=True, default=0)
    lfk = db.Column(db.Integer, nullable=True, default=0)
    cooking = db.Column(db.Integer, nullable=True, default=0)
    buyfood = db.Column(db.Integer, nullable=True, default=0)
    cleaning = db.Column(db.Integer, nullable=True, default=0)
    walking = db.Column(db.Integer, nullable=True, default=0)
    client_age = db.Column(db.Integer, nullable=False, default=0)
    worker_id = db.Column(db.Integer, db.ForeignKey('worker.id'))


