from infrastructure.database.base_setup import BaseSetup
from infrastructure.database.constants import *
from model.DTOs.food_routine_dto import FoodRoutineDTO
from utils.helper import Helper
from typing import List
import sqlite3, datetime, bcrypt

class FoodRoutineSetup(BaseSetup):
    
    def view(dog_id: str):
        conn = BaseSetup.connect()
        
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM {} WHERE dog_id = ?".format(FOOD_ROUTINE_TABLE), (dog_id,))
        
        rows = cur.fetchall()
        
        food_routines = [] 

        for row in rows:
            food_routine = FoodRoutineDTO(row[0], row[1], row[2], row[3])
            food_routines.append(food_routine.to_dict())
            
        BaseSetup.close(conn)
        
        return food_routines
   