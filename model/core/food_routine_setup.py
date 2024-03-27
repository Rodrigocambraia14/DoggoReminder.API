from infrastructure.database.base_setup import BaseSetup
from infrastructure.database.constants import *
from model.DTOs.food_routine_dto import FoodRoutineDTO
from model.DTOs.portion_detail_dto import PortionDetailDTO
from utils.helper import Helper
from typing import List
import sqlite3, bcrypt
from datetime import datetime

class FoodRoutineSetup(BaseSetup):
    
    @staticmethod
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
   
    @staticmethod
    def throw_notifications():
        
        current_time = datetime.now().strftime('%H:%M')  

        conn = BaseSetup.connect()
        
        cur = conn.cursor()
        
        cur.execute("""
    SELECT {}.*, {}.name AS dog_name
    FROM {} 
    INNER JOIN {} ON {}.dog_id = {}.id
""".format(FOOD_ROUTINE_TABLE, DOG_TABLE, FOOD_ROUTINE_TABLE, DOG_TABLE, FOOD_ROUTINE_TABLE, DOG_TABLE))
        
        rows = cur.fetchall()
        
        for row in rows:
            food_routine = FoodRoutineDTO(row[0], row[1], row[2], row[3])
            
            dog_name = row[4]
            
            cur.execute("""
            SELECT *
            FROM {}
            WHERE food_routine_id = ?            
            """.format(PORTION_DETAIL_TABLE), (food_routine.id,))
        
            portion_detail_rows = cur.fetchall()
            
            for portion_detail_row in portion_detail_rows:
                portion_detail = PortionDetailDTO(portion_detail_row[0], portion_detail_row[1], portion_detail_row[2], portion_detail_row[3], portion_detail_row[4])
                

                if portion_detail.feed_time == current_time:
                    message = f"DOGGO ALERT! {dog_name} esta com fome, Coloque {portion_detail.grams} gramas de racao as {portion_detail.feed_time}h!"
                    print(message)  
            
        BaseSetup.close(conn)
        
        return