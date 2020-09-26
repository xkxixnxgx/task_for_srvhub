from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from webapp.user.views import blueprint as user_blueprint
from webapp.pictures.views import blueprint as picture_blueprint
from webapp.comments.views import blueprint as comments_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db = SQLAlchemy()
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(picture_blueprint)
    app.register_blueprint(comments_blueprint)

    @app.route('/')
    def index():
        render_template('pictures.html')





