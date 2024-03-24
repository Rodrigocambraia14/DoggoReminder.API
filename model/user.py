from infrastructure.database.setup import Setup
from model.common.entity import Entity
from utils.helper import Helper

class User(Entity):

    def __init__(self, name, email, password):
        self.id = Helper.get_new_id()
        self.name = name
        self.email = email
        self.password = password
        
    def add(self):
        Setup.insert(self)