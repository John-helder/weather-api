import requests
from datetime import datetime
from app.database import insert_weather_data

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    
def fetch_and_save_weather(city):
    weather_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric&lang=pt_br"
    response = requests.get( weather_url)

    if response.status_code == 200:
        data = response.json()

        city_name = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        insert_weather_data(city_name, temperature, humidity, description, date)
        print(f" Dados salvos para {city_name}")
    else:
        print(f" Erro {response.status_code}: {response.text}")
