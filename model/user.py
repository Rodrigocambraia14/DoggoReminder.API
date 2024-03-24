from model.core.user_setup import UserSetup
from infrastructure.database.base_setup import BaseSetup
from model.common.entity import Entity
from utils.helper import Helper
from infrastructure.database.constants import *

class User(Entity):

    def __init__(self, new_id, name, email, password):
        self.id = new_id
        self.name = name
        self.email = email
        self.password = password
        
    def add(self):
        BaseSetup.insert(USER_TABLE, self)

    def list():
        return UserSetup.view()

    def login(email: str, password : str):
        return UserSetup.view()