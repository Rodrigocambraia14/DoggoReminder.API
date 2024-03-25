from abc import ABC, abstractmethod
import sqlite3, datetime
from infrastructure.database.constants import *

class BaseSetup(ABC):

    @staticmethod
    def start_seed():
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        name TEXT,
        email TEXT,
        password TEXT
    )
""")

        cur.execute("""
    CREATE TABLE IF NOT EXISTS dogs (
        id TEXT PRIMARY KEY,
        name TEXT,
        race TEXT,
        age INTEGER,
        gender TEXT,
        color TEXT,
        user_id TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
""")
        
        cur.execute("""
    CREATE TABLE IF NOT EXISTS food_routines (
        id TEXT PRIMARY KEY,
        name TEXT,
        portions INTEGER,
        dog_id TEXT,
        FOREIGN KEY (dog_id) REFERENCES dogs(id)
    )
""")
        
        cur.execute("""
    CREATE TABLE IF NOT EXISTS portion_details (
        id TEXT PRIMARY KEY,
        name TEXT,
        grams INTEGER,
        feed_time TEXT,
        food_routine_id TEXT,            
        FOREIGN KEY (food_routine_id) REFERENCES food_routines(id)
    )
""")
        conn.commit()
        conn.close()
        #TODO - Finish the seed

        # for i in books:
        #     bk = Book(get_new_id(), i['available'], i['title'], i['timestamp'])
        #     insert(bk)

    @staticmethod
    def insert(table_name : str, obj):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        # Assuming obj attributes correspond to table columns
        placeholders = ','.join(['?'] * len(obj.__dict__.keys()))
        columns = ','.join(obj.__dict__.keys())
        values = tuple(obj.__dict__.values())
        
        cur.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", values)
        
        conn.commit()
        conn.close()
        
    @abstractmethod
    def view(self):
        pass
    
    @staticmethod
    def connect():
        conn = sqlite3.connect(DB_NAME)
        return conn
   
    @staticmethod
    def close(conn: sqlite3.Connection):
        conn.close()
        
    @staticmethod
    def commitAndClose(conn: sqlite3.Connection):
        conn.commit()
        conn.close()

    @staticmethod
    def update(book):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("UPDATE books SET available=?, title=? WHERE id=?", (book.available, book.title, book.id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(theId):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("DELETE FROM books WHERE id=?", (theId,))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_all():
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("DELETE FROM books")
        conn.commit()
        conn.close()