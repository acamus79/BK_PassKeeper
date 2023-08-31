from flask import Blueprint, jsonify
# Modelos
from models.PasswordModel import PasswordModel

main = Blueprint('password_blueprint', __name__)

@main.route('/')
def get_pass():
    try:
        return jsonify(PasswordModel.get_all_passwords())
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
