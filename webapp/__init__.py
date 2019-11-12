from flask import Flask, render_template, flash, redirect, url_for, request


def create_app():
    app = Flask(__name__)

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

    return app
