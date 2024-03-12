# article_model

from .. import db, marsh
import datetime


class Article(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100))
    Description = db.Column(db.Text)
    CreatedOn = db.Column(db.DateTime, default=datetime.datetime.now())


class ArticleSchema(marsh.Schema):
    class Meta:
        fields = ('Id', 'Title', 'Description', 'CreatedOn')


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

