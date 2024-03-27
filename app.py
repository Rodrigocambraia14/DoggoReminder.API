# -*- coding: utf-8 -*-
from flask import Flask, jsonify, Response
from api.controllers.user_controller import user_controller
from api.controllers.dog_controller import dog_controller
from api.controllers.food_routine_controller import food_routine_controller
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from infrastructure.database.constants import *
from infrastructure.database.base_setup import BaseSetup
from model.core.food_routine_setup import FoodRoutineSetup
import json, os, schedule, threading
import sqlite3, datetime
from model.entities.user import User
from model.entities.dog import Dog
from model.entities.food_routine import FoodRoutine
from model.entities.portion_detail import PortionDetail
from utils.helper import Helper

app = Flask(__name__)

app.register_blueprint(user_controller, url_prefix='/api')
app.register_blueprint(dog_controller, url_prefix='/api')
app.register_blueprint(food_routine_controller, url_prefix='/api')

CORS(app)

# Configure Swagger UI
SWAGGER_URL = '/swagger'
API_URL = 'http://127.0.0.1:5000/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API da DoggoReminderUI"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def swagger():
    with open('swagger.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return jsonify(data)
    

if not os.path.isfile(DB_NAME):
    BaseSetup.create_tables()
    
    #start seed below
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
        
    user = User(Helper.get_new_id(), 'PUC RIO', 'tester@PUCRIO.com', 'PUC@123')
    user.add()
     
    dog = Dog(Helper.get_new_id(), 'Abigail', 'Beagle', 1, 'F', 'Tricolor', user.id)
    dog.add()
        
    food_routine = FoodRoutine(Helper.get_new_id(), 'alimentacao Abigail', 3, dog.id)
    food_routine.add()
        
    first_portion_detail = PortionDetail(Helper.get_new_id(), 'cafe da manha', 200, '09:00', food_routine.id)
    second_portion_detail = PortionDetail(Helper.get_new_id(), 'almoco', 200, '13:00', food_routine.id)
    third_portion_detail = PortionDetail(Helper.get_new_id(), 'janta', 200, '20:00', food_routine.id)
    fourth_portion_detail = PortionDetail(Helper.get_new_id(), 'ceia', 200, '23:43', food_routine.id)
        
    first_portion_detail.add()
    second_portion_detail.add()
    third_portion_detail.add()
    fourth_portion_detail.add()

    conn.commit()
    conn.close()
    #end seed
    
schedule.every().minute.do(FoodRoutineSetup.throw_notifications)

# Function to run the scheduler in a background thread
def run_scheduler():
    while True:
        schedule.run_pending()

# Start the scheduler in a background thread
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()

app.run()