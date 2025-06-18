# app.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class WeatherData(BaseModel):
    location: str
    weatherCode: int
    temperature: float
    wind: float
    isDay: int

@app.post("/collect")
async def collect_data(data: WeatherData):
    print("Received data:")
    print(f"Location: {data.location}, WeatherCode: {data.weatherCode}, Temp: {data.temperature}, Wind: {data.wind}, IsDay: {data.isDay}")
    return {"status": "success"}
