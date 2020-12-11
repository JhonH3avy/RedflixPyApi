from typing import Optional
from fastapi import FastAPI
import mariadb
import sys

app = FastAPI()

def connect_to_db():
    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user="db_user",
            password="db_user_passwd",
            host="192.0.2.1",
            port=3306,
            database="employees"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    return conn.cursor()

def get_users(cursor):
    return cursor.execute("SELECT * FROM users")

def get_user_by_id(cursor, id):
    return cursor.execute("SELECT * FROM users WHERE id=?", (id,))

cur = connect_to_db()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}