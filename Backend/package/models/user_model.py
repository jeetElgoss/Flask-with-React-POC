from .. import db, marsh
from datetime import datetime


class User(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.String(100), unique=True)
    CreatedOn = db.Column(db.DateTime, default=datetime.now())


class UserSchema(marsh.Schema):
    class Meta:
        fields = ('Id', 'Email', 'CreatedOn')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
