from ..models.user_model import User, user_schema, users_schema
from .. import db
from flask import jsonify, request
from datetime import datetime

""" storing time stamp value """
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class UserService:
    def get_all_users(self):
        """Get all articles."""
        try:
            records = User.query.all()
            if records:
                result = users_schema.dump(records)
                return jsonify({"data": result, "status_code": 200, "timestamp": timestamp}), 200
            else:
                return jsonify({"message": "No record available.", "status_code": 404, "timestamp": timestamp}), 404
        except Exception as ex:
            return self.handle_error(ex)

    def add_users(user_json_data):
        pass

    def handle_error(self, ex):
        """Handle errors."""
        error_message = f"There is a problem in endpoint: {ex}"
        return jsonify({"message": error_message, "status_code": 500, "timestamp": timestamp}), 500
