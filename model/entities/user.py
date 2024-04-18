import bcrypt
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
    
        self.password = Helper.hash_password(self.password)
    
        BaseSetup.insert(USER_TABLE, self)

    @staticmethod
    def login(email: str, password : str):
        return UserSetup.login(email, password)