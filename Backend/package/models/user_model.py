# user_model

from .. import db, marsh
from datetime import datetime


class User(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    PublicId = db.Column(db.String(100), unique=True)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    Password = db.Column(db.String(64), nullable=False)
    CreatedOn = db.Column(db.DateTime, default=datetime.now())


user_model = User()


class UserSchema(marsh.Schema):
    class Meta:
        fields = ('Id', 'PublicId', 'Email', 'Password', 'CreatedOn')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
