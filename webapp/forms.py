from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField


class ProfileForm(FlaskForm):
    lastname = StringField(
        'Фамилия',
        render_kw={
            "class": "form-control",
            "type": "text"})

    name = StringField(
        'Имя',
        render_kw={
            "class": "form-control",
            "type": "text"})

    fathername = StringField(
        'Отчетство',
        render_kw={
            "class": "form-control",
            "type": "text"})

    birthdat = DateField(
        'Дата рождения',
        render_kw={
            "class": "form-control date",
            "type": "date"})

    submit_search = SubmitField(
        'Зарегистрироваться',
        render_kw={"class": "btn btn-primary", "type": "submit"})
