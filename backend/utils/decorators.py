from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from flask import jsonify
from functools import wraps

def role_required(role_name):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt_identity() # Assumir que eu armazeno o role nas claims
            if "role" not in claims or claims["role"] != role_name:
                return jsonify({"message": "Acesso nao autorizado: permissao insuficiente"}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper