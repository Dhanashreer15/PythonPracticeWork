from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from extension import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"msg": "Missing JSON body"}), 400

    hashed_pw = generate_password_hash(data['password'])
    user = User(
        username=data['username'],
        email=data['email'],
        password=hashed_pw,
        role=data['role']
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"msg": "Missing JSON body"}), 400

    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        token = create_access_token(identity=str(user.id))
        return jsonify(access_token=token)
    return jsonify({"msg": "Invalid credentials"}), 401