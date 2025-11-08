from app.dataWeather import fetch_and_save_weather
from app.database import create_table

if __name__ == "__main__":
    create_table()
    fetch_and_save_weather("Castanhal")



