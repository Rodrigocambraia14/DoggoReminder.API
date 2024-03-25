# -*- coding: utf-8 -*-
from flask import Flask, jsonify, Response
from api.controllers.user_controller import user_controller
from api.controllers.dog_controller import dog_controller
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from infrastructure.database.constants import *
from infrastructure.database.base_setup import BaseSetup
import json, os

app = Flask(__name__)

app.register_blueprint(user_controller, url_prefix='/api')
app.register_blueprint(dog_controller, url_prefix='/api')

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
    BaseSetup.start_seed()

app.run()