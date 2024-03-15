# __init__ package directory

from flask import Flask
from flask_cors import CORS

from .extensions import db, migrate, marsh
from .config import Config


def create_app():
    app = Flask(__name__)
    try:
        # To stop Preventing request by browser
        CORS(app)
        # Creating db connection
        app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URL
        app.config['SECRET_KEY'] = Config.SECRET_KEY
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)
        # Connection code line is completed here

        migrate.init_app(app, db)
        marsh.init_app(app)
        # calling models here

        from .models.article_model import Article
        from .models.user_model import User

        # Return the Flask application object
        return app
    except Exception as e:
        # Let exceptions propagate
        raise e

