from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Backend.config import Config
from flask_migrate import Migrate

# instantiating flask object
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URL
app.config['SECRET_KEY'] = Config.SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
print(Config.SECRET_KEY)
