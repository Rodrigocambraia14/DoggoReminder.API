from flask import Flask
from api.controllers import user_controller


app = Flask(__name__)

app.register_blueprint(user_controller)

app.run()