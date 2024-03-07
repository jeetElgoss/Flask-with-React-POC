from Backend.package import db
import datetime


class Article(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100))
    Description = db.Column(db.Text)
    CreatedOn = db.Column(db.Datetime, default=datetime.datetime.now())
