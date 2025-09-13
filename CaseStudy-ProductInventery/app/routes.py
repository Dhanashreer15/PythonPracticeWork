from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Category, Product, User
from extension import db

routes_bp = Blueprint('routes', __name__)

def role_required(required_role):
    def wrapper(fn):
        @jwt_required()
        def decorator(*args, **kwargs):
            user_id = int(get_jwt_identity())
            user = User.query.get(user_id)
            if user and user.role == required_role:
                return fn(*args, **kwargs)
            return jsonify({"msg": "Access denied"}), 403
        decorator.__name__ = fn.__name__
        return decorator
    return wrapper

@routes_bp.route('/categories', methods=['POST'])
@role_required('admin')
def create_category():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"msg": "Missing category name"}), 400
    category = Category(name=data['name'], description=data.get('description'))
    db.session.add(category)
    db.session.commit()
    return jsonify({"msg": "Category created"}), 201

@routes_bp.route('/categories', methods=['GET'])
@jwt_required()
def get_categories():
    categories = Category.query.all()
    result = [{"id": c.id, "name": c.name, "description": c.description} for c in categories]
    return jsonify(result)

@routes_bp.route('/categories/<int:id>', methods=['DELETE'])
@role_required('admin')
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({"msg": "Category deleted"})

@routes_bp.route('/products', methods=['POST'])
@role_required('admin')
def create_product():
    data = request.get_json()
    required_fields = ['name', 'price', 'stock', 'category_id']
    if not data or not all(field in data for field in required_fields):
        return jsonify({"msg": "Missing product fields"}), 400
    product = Product(**data)
    db.session.add(product)
    db.session.commit()
    return jsonify({"msg": "Product created"}), 201

@routes_bp.route('/products', methods=['GET'])
@jwt_required()
def get_products():
    products = Product.query.all()
    result = [{
        "id": p.id, "name": p.name, "price": float(p.price),
        "stock": p.stock, "category": p.category.name
    } for p in products]
    return jsonify(result)

@routes_bp.route('/products/<int:id>', methods=['PUT'])
@role_required('admin')
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    product.price = data.get('price', product.price)
    product.stock = data.get('stock', product.stock)
    db.session.commit()
    return jsonify({"msg": "Product updated"})

@routes_bp.route('/products/<int:id>', methods=['DELETE'])
@role_required('admin')
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"msg": "Product deleted"})

@routes_bp.route('/products/category/<int:category_id>', methods=['GET'])
@jwt_required()
def filter_products_by_category(category_id):
    products = Product.query.filter_by(category_id=category_id).all()
    result = [{
        "id": p.id, "name": p.name, "price": float(p.price),
        "stock": p.stock, "category": p.category.name
    } for p in products]
    return jsonify(result)

@routes_bp.route('/products/search', methods=['GET'])
@jwt_required()
def search_products():
    name_query = request.args.get('name', '')
    products = Product.query.filter(Product.name.ilike(f"%{name_query}%")).all()
    result = [{
        "id": p.id, "name": p.name, "price": float(p.price),
        "stock": p.stock, "category": p.category.name
    } for p in products]
    return jsonify(result)