from flask import Flask
from flask_restx import Api
from .views import api
from .config import Config
# from models import Review, Book
from .database import db
# from views.books import book_ns
# from views.reviews import review_ns

def create_app(config):
    new_app = Flask(__name__)
    new_app.config.from_object(config)
    new_app.app_context().push()
    return new_app

def config_app(app):
    db.init_app(app)
    api.init_app(app)


if __name__ == '__main__':
    app = create_app(Config())
    config_app(app)
    app.debug = True
    app.run(host="localhost", port=10001, debug=True)
