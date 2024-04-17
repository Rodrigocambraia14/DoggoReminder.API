import bcrypt
from model.DTOs.dog_dto import DogDTO
from model.core.dog_setup import DogSetup
from model.core.user_setup import UserSetup
from infrastructure.database.base_setup import BaseSetup
from model.common.entity import Entity
from utils.helper import Helper
from infrastructure.database.constants import *

class Dog(Entity):

    def __init__(self, new_id, name, race, age, gender, color, user_id):
        self.id = new_id
        self.name = name
        self.race = race
        self.age = age
        self.color = color
        self.gender = gender
        self.user_id = user_id
        
    def add(self):
        BaseSetup.insert(DOG_TABLE, self)
    
    def update(self):
        
        updated_dog = DogDTO(self.id, self.name, self.race, self.age, self.gender, self.color, self.user_id)  
        
        DogSetup.update(updated_dog)

    def list(user_id: str):
        return DogSetup.view(user_id)
    
    @staticmethod
    def delete(dog_id: str):
        return DogSetup.delete(dog_id)
