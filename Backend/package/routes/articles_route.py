# Articles_route.py
from flask import Blueprint

article_bp = Blueprint('articles', __name__)


@article_bp.route('/')
def home():
    return 'Hello, welcome to the test home page!'


@article_bp.route('/about')
def about():
    return 'This is the test about page.'
