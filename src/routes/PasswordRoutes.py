from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required, verify_jwt_in_request

#Entidades
from entities.Password import Password
# Modelos
from services.PasswordService import PasswordService

main = Blueprint('password_blueprint', __name__)

@main.route('/')
def get_all():
    try:
        return jsonify(PasswordService.get_all_passwords())
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/<id>')
def get_one(id):
    try:
        password = PasswordService.get_password_byID(id)
        if password != None:
            return jsonify(password)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/add', methods = ['POST'])
@jwt_required()
def add_pwd():
    # Obtén los datos del cuerpo de la solicitud POST
    data = request.json
    #Si no se envia request
    if data:
        current_user = get_jwt_identity()
        # Crea una instancia de la clase Password con los datos proporcionados
        password = Password(data['url'], data['username'], data['keyword'], data['description'], data['category'], current_user['user_id'])
    else:
        return jsonify({'error': 'No se proporcionaron datos válidos en la solicitud'}), 400

    # Agrega la contraseña a la base de datos utilizando el modelo
    try:
        rows_affected = PasswordService.add_password(password)
        if rows_affected > 0:
            return jsonify({'message': 'Contraseña agregada correctamente'}), 201
        else:
            return jsonify({'message': 'No se pudo agregar la contraseña'}), 500
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
