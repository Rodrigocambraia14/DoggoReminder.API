from infrastructure.database.base_setup import BaseSetup
from infrastructure.database.constants import *
from model.DTOs.user_dto import UserDTO
from typing import List
import sqlite3, datetime

class UserSetup(BaseSetup):
    
    def view():
        conn = BaseSetup.connect()
        
        cur = conn.cursor()
        
        cur.execute(f"SELECT * FROM {USER_TABLE}")
        
        rows = cur.fetchall()
        
        users = [] 

        for row in rows:
            user = UserDTO(row[0], row[1], row[2], row[3])
            users.append(user.to_dict())
            
        BaseSetup.close(conn)
        
        return users