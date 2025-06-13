from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not all([username, email, password]):
        return jsonify({"message": "Dados incompletos."}), 400

    user, error = AuthService.register_user(username, email, password)
    if error:
        return jsonify({"message": error}), 409 # Conflict
    return jsonify({"message": "Usuario registrado com sucesso", "user_id": user.id}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not all([username, password]):
        return jsonify({"message": "Nome de usuario ou senha ausentes."}), 400

    tokens, error = AuthService.login_user(username, password)
    if error:
        return jsonify({"message": error}), 401
    return jsonify(tokens), 200

# Rota protegida com JWT
from flask_jwt_extended import jwt_required, get_jwt_identity

@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected_route():
    current_user_identity = get_jwt_identity()
    return jsonify(logged_in_as=current_user_identity), 200