from Backend.main import db
import datetime


class TArticle(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100))
    Description = db.Column(db.Text)
    CreatedOn = db.Column(db.DateTime, default=datetime.datetime.now())
