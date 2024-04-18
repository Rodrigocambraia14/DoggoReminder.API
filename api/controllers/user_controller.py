from utils.helper import Helper
from flask import Blueprint, jsonify, request
from model.entities.user import User

user_controller = Blueprint('user_controller', __name__)

@user_controller.route("/user/add", methods=['POST'])
def user_add():
    
    required_params = ['name', 'email', 'password']
    if not all(param in request.json for param in required_params):
        return jsonify({'error': 'Alguns parametros nao foram preenchidos corretamente!'}), 400

    name = request.json['name']
    email = request.json['email']
    password = request.json['password']

    user = User(Helper.get_new_id(), name, email, password)
    user.add()

    return jsonify({'message': 'Usuario adicionado com sucesso.'}), 201

@user_controller.route("/user/login", methods=['POST'])
def user_login():
    
    required_params = ['email', 'password']
    if not all(param in request.json for param in required_params):
        return jsonify({'error': 'Alguns parametros nao foram preenchidos corretamente!'}), 400

    email = request.json['email']
    password = request.json['password']

    user = User.login(email, password)

    return jsonify(user), 200
