# Articles_route.py

from flask import url_for, redirect, Blueprint
from ..models.article_model import Article, articles_schema, article_schema
from flask import jsonify

article_bp = Blueprint('article', __name__)


@article_bp.route('/', methods=['GET', 'POST'])
def index():
    records = Article.query.all()
    result = articles_schema.dump(records)
    return jsonify(result)
