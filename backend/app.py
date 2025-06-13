from flask import Flask, jsonify
from config import DevelopmentConfig, ProductionConfig
from extensions import db, jwt, cors
from routes.auth import auth_bp
from routes.users import users_bp
#from routes.products import products_bp
#from routes.orders import orders_bp

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    # Registra Blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(users_bp, url_prefix='/api/users')
#    app.register_blueprint(products_bp, url_prefix='/api/products')
#    app.register_blueprint(orders_bp, url_prefix='/api/orders')

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"message": "Recurso nao encontrado"}), 404

    @app.errorhandler(400)
    def bad_request_error(error):
        return jsonify({"message": "Requisição invalida"}), 400

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)