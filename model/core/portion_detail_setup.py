from infrastructure.database.base_setup import BaseSetup
from infrastructure.database.constants import *
from model.DTOs.portion_detail_dto import PortionDetailDTO

class PortionDetailSetup(BaseSetup):
    
    @staticmethod
    def view(food_routine_id: str):
        conn = BaseSetup.connect()
        
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM {} WHERE food_routine_id = ?".format(PORTION_DETAIL_TABLE), (food_routine_id,))
        
        rows = cur.fetchall()
        
        portion_details = [] 

        for row in rows:
            portion_detail = PortionDetailDTO(row[0], row[1], row[2], row[3], row[4])
            portion_details.append(portion_detail.to_dict())
            
        BaseSetup.close(conn)
        
        return portion_details
   