# Rutas de la api para users

from flask import Blueprint, jsonify, request
from database import db
from .models import User

# blueprint de usuarios
users_bp = Blueprint('users', __name__)

# Read/get users from database
@users_bp.route('/', methods=['GET'])
def get_user():
    user = User.query.all()
    return jsonify([
        {
            'id': u.id,
            'name': u.name,
            'email': u.email,
            'role': u.role
        } for u in user
    ]), 200

""" get_users Sin compresion de listas
@users_bp.route('/', methods=['GET'])
def get_user():
    user = User.query.all()
    result = []
    for u in user:
        result.append({
            'id': u.id,
            'name': u.name,
            'email': u.email,
            'role': u.role
        })
    return jsonify(result), 200
    
"""    

# Create/post user to database
@users_bp.route('/', methods=['POST'])
def create_user():
    # Lectura de la peticion y transformacion a json
    data = request.get_json()
    # Creacion del nuevo usuario
    new_user = User(
        name=data['name'],
        email=data['email'],
        role=data['role']
    )
    
    # Almacenamiento del nuevo usuario en la bd
    db.session.add(new_user)
    db.session.commit()
    
    # Respuesta de creacion
    return jsonify({
        'message': 'Usuario creado exitosamente',
        'user': {
            'id': new_user.id,
            'name': new_user.name,
            'email': new_user.email,
            'role': new_user.role
        }
    }), 201