from sqlalchemy.exc import IntegrityError

from ..models.user_model import User, user_schema, users_schema
from .. import db
from flask import jsonify
from datetime import datetime
import uuid
from werkzeug.security import generate_password_hash

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

    def add_user(self, json_data):
        try:
            public_id = str(uuid.uuid4())
            email = json_data.get("email")
            password = json_data.get("password")
            hash_password = generate_password_hash(password)
            new_user = User(PublicId=public_id, Email=email, Password=hash_password)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"message": "User created successfully.", "status_code": 200, "timestamp": timestamp}), 200
        except IntegrityError:
            db.session.rollback()  # Rollback the session to prevent partial updates
            return jsonify({"error": "Email already exists", "status_code": 400, "timestamp": timestamp}), 400
        except Exception as ex:
            return self.handle_error(ex)

    def get_user_by_id(self, user_id):
        """Get user by id."""
        try:
            print("user id :", user_id)
            records = User.query.filter_by(Id=user_id).first()
            if records:
                result = user_schema.dump(records)
                return jsonify({"data": result, "status_code": 200, "timestamp": timestamp}), 200
            else:
                return jsonify({"message": "No record available.", "status_code": 404, "timestamp": timestamp}), 404
        except Exception as ex:
            return self.handle_error(ex)

    def handle_error(self, ex):
        """Handle errors."""
        error_message = f"There is a problem in endpoint: {ex}"
        return jsonify({"message": error_message, "status_code": 500, "timestamp": timestamp}), 500
