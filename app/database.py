import sqlite3

DB_NAME = "app/data/weather.db"

def create_connection():
    conn = sqlite3.connect("app/data/weather.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            humidity INTEGER,
            description TEXT,
            date TEXT
        )
    ''')

    conn.commit()
    conn.close()

def insert_weather_data(city, temperature, humidity, description, date):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO weather (city, temperature, humidity, description, date)
        VALUES (?, ?, ?, ?, ?)
    ''', (city, temperature, humidity, description, date))

    conn.commit()
    conn.close()

def get_all_weather_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM weather")
    rows = cursor.fetchall()

    conn.close()

    data = [
        {
            "id": row[0],
            "city": row[1],
            "temperature": row[2],
            "humidity": row[3],
            "description": row[4],
            "date": row[5],
        }
        for row in rows
    ]
    return data
