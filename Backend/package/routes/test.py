# test.py
from flask import Blueprint

test_bp = Blueprint('test', __name__)


@test_bp.route('/')
def home():
    return 'Hello, welcome to the home page!'


@test_bp.route('/about')
def about():
    return 'This is the about page.'
