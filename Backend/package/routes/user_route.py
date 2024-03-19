from flask import Blueprint, request
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
    result = user_obj.add_user(json_data)
    return result


@user_bp.route("/get_user_by_id/<user_id>", methods=["GET"])
def get_user_by_id(user_id):
    result = user_obj.get_user_by_id(user_id)
    return result


@user_bp.route("/update_user/<public_id>", methods=["PUT"])
def update_user(public_id):
    json_data = request.get_json()
    return user_obj.update_user(public_id, json_data)


@user_bp.route("/delete_user/<public_id>", methods=["DELETE"])
def delete_user(public_id):
    return user_obj.delete_user(public_id)


@user_bp.route("/login")
def login():
    auth_data = request.authorization
    result = user_obj.login(auth_data)
    return result
