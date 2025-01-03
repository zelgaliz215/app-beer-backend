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
            'role': u.role,
            'date_created': u.created_at
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
    

# Get user by id
@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        return {"user": user.to_dict()}, 200
    return {"error": "User not found"}, 404

    
# Update/put user in database
@users_bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    # Busqueda del usuario en la bd
    user = User.query.get_or_404(id)
    # Lectura de la peticion en json
    data = request.get_json()
    
    # Validacion de existencia del usuario
    if not user:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    
    name = data.get('name')
    email = data.get('email')
    role = data.get('role')
    
    # Actualizacion de de los datos del usuario
    if name:
        user.name = name
    if email:
        user.email = email
    if role:
        user.role = role
    
    # Almacenamiento de los cambios en la bd
    db.session.commit()
    
    # Respuesta de actualización
    return jsonify({
        'message': 'Usuario actualizado exitosamente',
        'user': {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'role': user.role,
            'create_at': user.created_at
        }
    }), 200
    

# Delete user from database
@users_bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    # Busqueda del usuario en la bd
    user = User.query.get_or_404(id)
    
    # Validacion de existencia del usuario
    if not user:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    
    # Eliminacion del usuario de la bd
    db.session.delete(user)
    db.session.commit()
    
    # Respuesta de eliminación
    return jsonify({
        'message': 'Usuario eliminado exitosamente',
        'user': user.id
    }), 204