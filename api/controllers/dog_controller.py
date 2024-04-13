from model.entities.dog import Dog
from utils.helper import Helper
from flask import Blueprint, jsonify, request
from model.entities.user import User
from flask import url_for

dog_controller = Blueprint('dog_controller', __name__)

@dog_controller.route("/dog/add", methods=['POST'])
def dog_add():
    
    required_params = ['name', 'race', 'age', 'gender', 'color', 'user_id']
    if not all(param in request.json for param in required_params):
        return jsonify({'error': 'Alguns parametros nao foram preenchidos corretamente!'}), 400

    name = request.json['name']
    race = request.json['race']
    age = request.json['age']
    gender = request.json['gender']
    color = request.json['color']
    user_id = request.json['user_id']
    
    dog = Dog(Helper.get_new_id(), name, race, age, gender, color, user_id)
    
    dog.add()

    return jsonify({'message': 'Pet adicionado com sucesso.'}), 201

@dog_controller.route("/dog/delete", methods=['POST'])
def dog_delete():
    
    required_params = ['dog_id']
    if not all(param in request.json for param in required_params):
        return jsonify({'error': 'Alguns parametros nao foram preenchidos corretamente!'}), 400

    dog_id = request.json['dog_id']
    
    Dog.delete(dog_id)
    
    return jsonify({'message': 'Pet removido com sucesso.'}), 200


@dog_controller.route("/dog/list", methods=['GET'])
def dog_list():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'O ID do usuario e obrigatorio.'}), 400
    
    dogs = Dog.list(user_id)
    
    return jsonify(dogs), 200
