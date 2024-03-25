import bcrypt
from model.core.portion_detail_setup import PortionDetailSetup
from infrastructure.database.base_setup import BaseSetup
from model.common.entity import Entity
from utils.helper import Helper
from infrastructure.database.constants import *

class PortionDetail(Entity):

    def __init__(self, new_id, name, grams, feed_time, food_routine_id):
        self.id = new_id
        self.name = name
        self.grams = grams
        self.feed_time = feed_time
        self.food_routine_id = food_routine_id
        
    def add(self):
        BaseSetup.insert(PORTION_DETAIL_TABLE, self)

    def list(food_routine_id: str):
        return PortionDetailSetup.view(food_routine_id)
