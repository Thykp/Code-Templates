from flask import Blueprint, jsonify
from app.services.user_service import get_user_by_id, get_all_users

user_blueprint = Blueprint("users", __name__)

@user_blueprint.route("/", methods=["GET"])
def list_users():
    users = [u.to_dict() for u in get_all_users()]
    return jsonify(users), 200

@user_blueprint.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({"error": "User not found"}), 404
