from fastapi import FastAPI, Query
from app.dataWeather import fetch_and_save_weather
from app.database import get_all_weather_data


app = FastAPI(title="Weather Data API")

@app.get("/")
def root():
    return {"message": "API rodando com sucesso!"}

@app.get("/weather")
def  get_weather(city: str = Query(..., description="Nome da Cidade")):
    try:
        fetch_and_save_weather(city)
        return {"message": f"Dados de {city} salvos com sucesso!"}
    except Exception as e:
        return {"erro": str(e)}
    
@app.get("/weather/all")
def list_weather():
    try:
        data = get_all_weather_data()
        return {"dados": data}
    except Exception as e:
        return{"erro": str(e)}
    