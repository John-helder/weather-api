import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def create_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id SERIAL PRIMARY KEY,
            city VARCHAR(100),
            temperature REAL,
            humidity INTEGER,
            description VARCHAR(255),
            date TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

def insert_weather_data(city, temperature, humidity, description, date):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO weather (city, temperature, humidity, description, date)
        VALUES (%s, %s, %s, %s, %s)
    """, (city, temperature, humidity, description, date))

    conn.commit()
    conn.close()

def get_all_weather_data():
    conn = create_connection()
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

if __name__ == "__main__":
    create_table()
    print(" Tabela 'weather' criada (ou já existia).")