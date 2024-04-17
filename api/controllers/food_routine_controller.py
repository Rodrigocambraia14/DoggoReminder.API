from model.entities.food_routine import FoodRoutine
from model.entities.portion_detail import PortionDetail
from utils.helper import Helper
from flask import Blueprint, jsonify, request

food_routine_controller = Blueprint('food_routine_controller', __name__)

@food_routine_controller.route("/food_routine/add", methods=['POST'])
def food_routine_add():
    
    required_params = ['name', 'portions', 'dog_id', 'portion_details']
    if not all(param in request.json for param in required_params):
        return jsonify({'error': 'Alguns parametros nao foram preenchidos corretamente!'}), 400

    name = request.json['name']
    portions = request.json['portions']
    dog_id = request.json['dog_id']
    portion_details = request.json['portion_details']
    
    food_routine = FoodRoutine(Helper.get_new_id(), name, portions, dog_id)
    
    food_routine.add()
    
    for item in portion_details:
        portion_detail = PortionDetail(Helper.get_new_id(), item['name'], item['grams'], item['feed_time'], food_routine.id)
        portion_detail.add()

    return jsonify({'message': 'Rotina adicionada com sucesso.'}), 201



@food_routine_controller.route("/food_routine/list", methods=['GET'])
def food_routine_list():
    
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({'error': 'Id do usuario e obrigatorio.'}), 400

    food_routines = FoodRoutine.list(user_id)
    
    return jsonify(food_routines), 200
