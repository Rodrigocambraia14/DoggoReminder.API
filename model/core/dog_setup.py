from infrastructure.database.base_setup import BaseSetup
from infrastructure.database.constants import *
from model.DTOs.dog_dto import DogDTO
from model.DTOs.user_dto import UserDTO
from utils.helper import Helper
from typing import List
import sqlite3, datetime, bcrypt

class DogSetup(BaseSetup):
    
    @staticmethod
    def view(user_id: str):
        conn = BaseSetup.connect()
        
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM {} WHERE user_id = ?".format(DOG_TABLE), (user_id,))
        
        rows = cur.fetchall()
        
        dogs = [] 

        for row in rows:
            dog = DogDTO(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            dogs.append(dog.to_dict())
            
        BaseSetup.close(conn)
        
        return dogs

    @staticmethod
    def delete(dog_id: str):
        conn = BaseSetup.connect()
        
        cur = conn.cursor()
        
        cur.execute("DELETE FROM {} WHERE id = ?".format(DOG_TABLE), (dog_id,))

        conn.commit()
        
        BaseSetup.close(conn)
        
        return
    
    @staticmethod
    def update(updated_dog: DogDTO):
        conn = BaseSetup.connect()
    
        cur = conn.cursor()
    
        query = "UPDATE {} SET name = ?, race = ?, age = ?, gender = ?, color = ? WHERE id = ?".format(DOG_TABLE)
    
        values = (updated_dog.name, updated_dog.race, updated_dog.age, updated_dog.gender, updated_dog.color, updated_dog.id)
    
        cur.execute(query, values)

        conn.commit()
    
        BaseSetup.close(conn)
    
        return
   