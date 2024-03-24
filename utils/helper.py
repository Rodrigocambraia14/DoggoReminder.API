import uuid

import bcrypt

class Helper:
    
    def get_new_id():
        return str(uuid.uuid4())
    
    def hash_password(password: str) -> str:
        # Convert password string to bytes
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        # Hash password
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        # Convert hashed password bytes back to string for storage
        return hashed_password.decode('utf-8')
    
    def check_password(password: str, hashed_password: str) -> bool:
        # Convert password string to bytes
        password_bytes = password.encode('utf-8')
        hashed_password_bytes = hashed_password.encode('utf-8')
        
        password_is_valid = bcrypt.checkpw(password_bytes, hashed_password_bytes)
        # Convert hashed password bytes back to string for storage
        return password_is_valid