from flask import Blueprint, jsonify, request
from model.user import User

user_controller = Blueprint('user_controller', __name__)

@user_controller.route("/user/add", methods=['POST'])
def user_add():
    
    required_params = ['name', 'email', 'password']

    if not all(param in request.json for param in required_params):
        return jsonify({'error': 'Alguns parâmetros não foram preenchidos corretamente!'}), 400

    name = request.json['name']
    email = request.json['email']
    password = request.json['password']

    user = User(name, email, password)
    user.add()

    return jsonify({'message': 'User added successfully'}), 200