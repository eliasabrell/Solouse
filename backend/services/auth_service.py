from models.user import User
from extensions import db
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta

class AuthService:
    @staticmethod
    def register_user(username, email, password):
        if User.query.filter_by(username=username).first():
            return None, "Nome de usuario ja existe."
        if User.query.filter_by(email=email).first():
            return None, "Email ja registrado."

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return new_user, None

    @staticmethod
    def login_user(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            access_token = create_access_token(identity={"id": user.id, "username": user.username, "role": "user"}, expires_delta=timedelta(hours=1))
            refresh_token = create_refresh_token(identity={"id": user.id})
            return {"access_token": access_token, "refresh_token": refresh_token}, None
        return None, "Credenciais invalidas."