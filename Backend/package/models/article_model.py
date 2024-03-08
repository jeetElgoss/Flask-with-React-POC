from .. import db
import datetime


class tbl_article(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100))
    Description = db.Column(db.Text)
    CreatedOn = db.Column(db.DateTime, default=datetime.datetime.now())


class tbl_user(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.String(100), unique=True)
    CreatedOn = db.Column(db.DateTime, default=datetime.datetime.now())