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
    json_data = request.get_json()
    print(json_data)
    result = user_obj.add_user(json_data)
    return result


@user_bp.route("/get_user_by_id/<user_id>", methods=["GET"])
def get_user_by_id(user_id):
    result = user_obj.get_user_by_id(user_id)
    return result

@user_bp.route("/delete_user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    return ""

@user_bp.route("/update_user/<user_id>", methods=["PUT"])
def update_user(user_id):
    return ""