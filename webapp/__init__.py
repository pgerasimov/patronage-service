from flask import Flask, render_template, flash, redirect, url_for, request


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        title = 'Патронаж Сервис'

        return render_template('index.html', page_title=title)

    @app.route('/patronage')
    def base_test():


        return render_template('patronazh.html')

    return app
