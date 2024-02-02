from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

WEATHER_API_KEY = "78d16053fec5e83e46ed380b9fe76814"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.get("/weather/")
async def get_weather(location: str):
    params = {
        "q": location,
        "appid": WEATHER_API_KEY,
        "units": "metric"  # or 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=404, detail="Weather data not found")
