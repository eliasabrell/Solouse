from flask import Blueprint, request, jsonify
from extensions import db
from models.order import Order
from flask_jwt_extended import jwt_required
from utils.decorators import role_required

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/", methods=["GET"])
def get_all_orders():
  orders = Order.query.all()
  return jsonify([order.to_dict() for order in orders]), 200