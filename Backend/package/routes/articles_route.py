# Articles_route.py

from flask import url_for, redirect, Blueprint, request
from ..models.article_model import Article, articles_schema, article_schema
from flask import jsonify
from .. import db

article_bp = Blueprint('article', __name__)


@article_bp.route('/get_article', methods=['GET'])
def get_article():
    try:
        records = Article.query.all()
        result = articles_schema.dump(records)
        return jsonify(result)
    except Exception as ex:
        return f"there is a problem in end point: {ex}"


@article_bp.route('/add_article', methods=['POST'])
def post_article():
    try:
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        created_on = data.get('created_on')
        article = Article(Title=title, Description=description, CreatedOn=created_on)
        db.session.add(article)
        db.session.commit()
        return article_schema.jsonify(article)
    except Exception as ex:
        return f"there is a problem in end point: {ex}"


@article_bp.route('/get_article_by_id/<article_id>', methods=['GET'])
def get_article_by_id(article_id):
    try:
        data = Article.query.filter_by(Id=article_id).first()
        result = article_schema.dump(data)
        return jsonify(result)
    except Exception as ex:
        return f"there is a problem in end point: {ex}"


@article_bp.route("/update_article/<article_id>", methods=["PUT"])
def update_article(article_id):
    try:
        data = Article.query.get(article_id)

        # getting data from http request
        json_data = request.get_json()
        data.Title = json_data.get('title')
        data.Description = json_data.get('description')
        data.CreatedOn = json_data.get('created_on')

        # updating query
        db.session.commit()
        return article_schema.jsonify(data)
    except Exception as ex:
        return f"there is a problem in end point: {ex}"


@article_bp.route("/delete_article/<article_id>", methods=["DELETE"])
def delete_article(article_id):
    try:
        article_data = Article.query.get(article_id)
        if article_data:
            db.session.delete(article_id)
            db.session.commit()
            return "Article deleted successfully"
        else:
            return f"No data found with article Id {article_id}."
    except Exception as ex:
        return f"there is a problem in end point: {ex}"
