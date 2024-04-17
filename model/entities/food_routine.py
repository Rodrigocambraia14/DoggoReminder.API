import bcrypt
from model.core.food_routine_setup import FoodRoutineSetup
from infrastructure.database.base_setup import BaseSetup
from model.common.entity import Entity
from utils.helper import Helper
from infrastructure.database.constants import *

class FoodRoutine(Entity):

    def __init__(self, new_id, name, portions, dog_id):
        self.id = new_id
        self.name = name
        self.portions = portions
        self.dog_id = dog_id
        
    def add(self):
        BaseSetup.insert(FOOD_ROUTINE_TABLE, self)

    def list(user_id: str):
        return FoodRoutineSetup.view(user_id)
