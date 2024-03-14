# article_service.py

from flask import jsonify
from .. import db
from ..models.article_model import Article, articles_schema, article_schema
from datetime import datetime

""" storing time stamp value """
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class ArticleService:
    def get_all_articles(self):
        """Get all articles."""
        try:
            records = Article.query.all()
            if records:
                result = articles_schema.dump(records)
                return jsonify({"data": result, "status_code": 200, "timestamp": timestamp}), 200
            else:
                return jsonify({"data": "No record available.", "status_code": 404, "timestamp": timestamp}), 404
        except Exception as ex:
            return self.handle_error(ex)

    def add_article(self, json_data):
        """Add a new article."""
        try:
            title = json_data.get('title')
            description = json_data.get('description')
            created_on = json_data.get('created_on')
            article = Article(Title=title, Description=description, CreatedOn=created_on)
            db.session.add(article)
            db.session.commit()
            return jsonify({"data": "Article added successfully.", "status_code": 200, "timestamp": timestamp}), 200
        except Exception as ex:
            db.session.rollback()
            return self.handle_error(ex)

    def get_article_by_id(self, article_id):
        """Get article by ID."""
        try:
            article_data = Article.query.get(article_id)
            if article_data:
                result = article_schema.dump(article_data)
                return jsonify({"data": result, "status_code": 200}), 200
            else:
                return jsonify({"data": f"No data found with article Id {article_id}.", "status_code": 404,
                                "timestamp": timestamp}), 404
        except Exception as ex:
            return self.handle_error(ex)

    def update_article(self, article_id, json_data):
        """Update article by ID."""
        try:
            article_data = Article.query.get(article_id)
            if article_data:
                article_data.Title = json_data.get('title')
                article_data.Description = json_data.get('description')
                article_data.CreatedOn = json_data.get('created_on')
                db.session.commit()
                return jsonify(
                    {"data": "Article updated successfully", "status_code": 200, "timestamp": timestamp}), 200
            else:
                return jsonify({"data": f"No data found with article Id {article_id}.", "status_code": 404,
                                "timestamp": timestamp}), 404
        except Exception as ex:
            return self.handle_error(ex)

    def delete_article(self, article_id):
        """Delete article by ID."""
        try:
            article_data = Article.query.get(article_id)
            if article_data:
                db.session.delete(article_data)
                db.session.commit()
                return jsonify(
                    {"data": "Article deleted successfully", "status_code": 200, "timestamp": timestamp}), 200
            else:
                return jsonify({"data": f"No data found with article Id {article_id}.", "status_code": 404,
                                "timestamp": timestamp}), 404
        except Exception as ex:
            return self.handle_error(ex)

    def handle_error(self, ex):
        """Handle errors."""
        error_message = f"There is a problem in endpoint: {ex}"
        return jsonify({"data": error_message, "status_code": 500, "timestamp": timestamp}), 500
