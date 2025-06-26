from flask import Blueprint, request, jsonify
from extensions import db
from models.product import Product
from flask_jwt_extended import jwt_required
from utils.decorators import role_required

products_bp = Blueprint("products", __name__)

@products_bp.route("/", methods=["GET"])
def get_all_products():
  products = Product.query.all()
  return jsonify([product.to_dict() for product in products]), 200