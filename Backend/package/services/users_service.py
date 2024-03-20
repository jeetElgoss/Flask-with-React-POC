from sqlalchemy.exc import IntegrityError
from Backend.package.models.user_model import User, user_schema, users_schema
from Backend.package import db, create_app
from flask import jsonify
from datetime import datetime, timedelta
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

app = create_app()

""" storing time stamp value """
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class UserService:
    def get_all_users(self):
        """Get all users."""
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
        """Add new user."""
        try:
            if "email" not in json_data or "password" not in json_data:
                return jsonify({"error": "Email and password are required fields.", "status_code": 400,
                                "timestamp": timestamp}), 400

            public_id = str(uuid.uuid4())
            email = json_data["email"]
            password = json_data["password"]
            if not email or not password:
                return jsonify(
                    {"error": "Email and password cannot be empty.", "status_code": 400, "timestamp": timestamp}), 400

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

    def get_user_by_id(self, public_id):
        """Get user by id."""
        try:
            records = User.query.filter_by(PublicId=public_id).first()
            if records:
                result = user_schema.dump(records)
                return jsonify({"data": result, "status_code": 200, "timestamp": timestamp}), 200
            else:
                return jsonify({"message": "No record available.", "status_code": 404, "timestamp": timestamp}), 404
        except Exception as ex:
            return self.handle_error(ex)

    def update_user(self, public_id, json_data):
        """Update user."""
        try:
            user = User.query.filter_by(PublicId=public_id).first()
            if not user:
                return jsonify(
                    {"data": False, "message": f"No data found.", "status_code": 404,
                     "timestamp": timestamp}), 404
            else:
                change_password = json_data.get("password")
                hash_password = generate_password_hash(change_password)
                user.Email = json_data.get("email")
                user.Password = hash_password
                db.session.commit()
                return jsonify({"Data": True, "message": "User updated successfully.", "status_code": 200,
                                "timestamp": timestamp}), 200
        except IntegrityError:
            db.session.rollback()  # Rollback the session to prevent partial updates
            return jsonify({"error": "Email already exists", "status_code": 400, "timestamp": timestamp}), 400
        except Exception as ex:
            return self.handle_error(ex)

    def delete_user(self, public_id):
        """Delete user by public_id."""
        try:
            records = User.query.filter_by(PublicId=public_id).first()
            if records:
                db.session.delete(records)
                db.session.commit()
                return jsonify({"data": True, "message": "User deleted successfully", "status_code": 200,
                                "timestamp": timestamp}), 200
            else:
                return jsonify(
                    {"data": False, "message": "No record available.", "status_code": 404, "timestamp": timestamp}), 404
        except Exception as ex:
            return self.handle_error(ex)

    def login(self, auth):
        try:
            if not auth or not auth.username or not auth.password:
                return jsonify({"message": "Invalid credentials.", "status_code": 401, "timestamp": timestamp}), 401

            user = User.query.filter_by(Email=auth.username).first()
            if not user:
                return jsonify({"message": "User not found.", "status_code": 401, "timestamp": timestamp}), 401

            if not check_password_hash(user.Password, auth.password):
                return jsonify({"message": "Incorrect password.", "status_code": 401, "timestamp": timestamp}), 401

            token = jwt.encode({'PublicId': user.PublicId, 'exp': datetime.now() + timedelta(minutes=30)},
                               app.config['SECRET_KEY'], algorithm='HS256')

            return jsonify({"token": token.decode('UTF-8'), "status_code": 200, "timestamp": timestamp}), 200

        except Exception as ex:
            # Handle any unexpected errors gracefully
            return self.handle_error(ex)

    def handle_error(self, ex):
        """Handle errors."""
        error_message = f"There is a problem in endpoint: {ex}"
        return jsonify({"message": error_message, "timestamp": timestamp, "status_code": 500}), 500
