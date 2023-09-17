from flask import Blueprint, jsonify, request
from util.JwtUtil import JwtUtil

#Entidades
from entities.User import User
# Modelos
from services.UserService import UserService

auth_routes = Blueprint('auth_blueprint', __name__)

@auth_routes.route('/register', methods=['POST'])
def create_user():
    data = request.json
    #Si no se envia request
    if not data:
        return jsonify({'error': 'No se proporcionaron datos válidos en la solicitud'}), 400
    else:
        # Crea una instancia de la clase User con los datos proporcionados
        user = User(data['email'], data['password'])
    try:
        user_add = UserService.sing_up(user)
        return jsonify({'token': JwtUtil.generate_jwt_token(user_add)}), 201
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@auth_routes.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No se proporcionaron datos válidos en la solicitud'}), 400
        
        user = UserService.get_user_by_email(data['email'])
        
        if user is None:
            return jsonify({'error': 'Email no encontrado'}), 401
        
        if data['password'] != user.password:
                return jsonify({'error': 'Contraseña incorrecta'}), 401
        else:
            token = JwtUtil.generate_jwt_token(user)
            return jsonify({'token': token}), 200
        
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
    
