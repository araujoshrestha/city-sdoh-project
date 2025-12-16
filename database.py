import sqlite3

DB_NAME = "cities.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_database():
    connect = get_connection()
    cursor = connect.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            state TEXT NOT NULL,
            city TEXT NOT NULL,
            population INTEGER,
            white INTEGER,
            black INTEGER,
            asian INTEGER,
            latin INTEGER,
            other INTEGER,
            low_food_access INTEGER,
            median_income INTEGER,
            poverty_rate REAL,
            unemployment_rate REAL       
                
                   
                          
    
                   
        )
    """)

    connect.commit()
    connect.close()