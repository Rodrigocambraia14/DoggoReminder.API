from infrastructure.database.base_setup import BaseSetup
from infrastructure.database.constants import *
from model.DTOs.user_dto import UserDTO
from utils.helper import Helper
from typing import List
import sqlite3, datetime, bcrypt

class UserSetup(BaseSetup):
    
    @staticmethod
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
    
    @staticmethod
    def login(email : str, password : str):
        
        conn = BaseSetup.connect()
        
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM {} WHERE email = ?".format(USER_TABLE), (email,))
        
        row = cur.fetchone()

        if row is None:
            BaseSetup.close(conn)
            raise Exception("Credenciais invalidas, nenhum usuario encontrado.")
        

        user = UserDTO(row[0], row[1], row[2], row[3])
        
        is_password_valid = Helper.check_password(password, user.password)

        if is_password_valid == False:
            BaseSetup.close(conn)
            raise Exception("Senha incorreta.")
        
        user = user.to_dict()
            
        BaseSetup.close(conn)
        
        return user['id']