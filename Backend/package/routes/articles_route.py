# articles_route.py

from flask import Blueprint, jsonify, request
from ..services.article_services import ArticleService

article_bp = Blueprint('article', __name__)
article_obj = ArticleService()


@article_bp.route('/get_article', methods=['GET'])
def get_article():
    """Get all articles."""
    return article_obj.get_all_articles()


@article_bp.route('/add_article', methods=['POST'])
def add_article():
    """Add a new article."""
    json_data = request.get_json()
    return article_obj.add_article(json_data)


@article_bp.route('/get_article_by_id/<article_id>', methods=['GET'])
def get_article_by_id(article_id):
    """Get article by ID."""
    return article_obj.get_article_by_id(article_id)


@article_bp.route("/update_article/<article_id>", methods=["PUT"])
def update_article(article_id):
    """Update article by ID."""
    json_data = request.get_json()
    return article_obj.update_article(article_id, json_data)


@article_bp.route("/delete_article/<int:article_id>", methods=["DELETE"])
def delete_article(article_id):
    """Delete article by ID."""
    return article_obj.delete_article(article_id)
