from flask_wtf import FlaskForm, validators
from wtforms import StringField, SubmitField, DateField, SelectField, TextAreaField


class ProfileForm(FlaskForm):
    lastname = StringField(
        'Фамилия*',
        render_kw={
            "class": "form-control",
            "type": "text"})

    name = StringField(
        'Имя*',
        render_kw={
            "class": "form-control",
            "type": "text"})

    fathername = StringField(
        'Отчетство',
        render_kw={
            "class": "form-control",
            "type": "text"})

    birthdate = DateField(
        'Дата рождения*',
        render_kw={
            "class": "form-control date",
        })

    gender = SelectField(choices=[('1', 'Мужской'), ('2', 'Женский')])

    bio = TextAreaField(u'Mailing Address'
                        'О себе',
                        render_kw={
                            "class": "form-control",
                            "type": "text",
                            "placeholder": "Расскажите кратко о себе и своем опыте"})

    submit_search = SubmitField(
        'Зарегистрироваться',
        render_kw={"class": "btn btn-primary", "type": "submit"})
