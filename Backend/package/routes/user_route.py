from flask import Blueprint, jsonify, request
from ..services.users_service import UserService

user_bp = Blueprint('user', __name__)

user_obj = UserService()


@user_bp.route("/users", methods=["GET"])
def get_all_users():
    result = user_obj.get_all_users()
    return result

@user_bp.route("/add_user", methods=["POST"])
def add_users():
    user_json_data = request.get_json()
    result = user_obj.get_all_users(user_json_data)
    return result