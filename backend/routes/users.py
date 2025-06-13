from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User
from flask_jwt_extended import jwt_required
from utils.decorators import role_required

users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["GET"])
@jwt_required()
@role_required("admin")
def get_all_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@users_bp.route("/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user_by_id(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict()), 200

@users_bp.route("/<int:user_id>", methods=["PUT"])
@jwt_required()
@role_required("admin")
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()

    if "username" in data:
        user.username = data["username"]
    if "email" in data:
        user.email = data["email"]
    if "password" in data:
        user.set_password(data["password"])

    db.session.commit()
    return jsonify({"message": "Usuario atualizado com sucesso", "user": user.to_dict()}), 200

@users_bp.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
@role_required("admin")
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Usuario deletado com sucesso"}), 204