#15. Hämta väderdata från en API och spara det i en fil.

import requests
import json
from datetime import datetime

# Din API-nyckel från OpenWeatherMap
API_KEY = "REDACTED"
CITY = "Kalmar"  # Staden du vill hämta väderdata för
UNITS = "metric"  # Använd "imperial" för Fahrenheit och miles
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}"

# Hämta väderdata
try:
    response = requests.get(URL)
    response.raise_for_status()  # Kasta ett undantag om något gick fel
    weather_data = response.json()
    
    # Skapa en fil för att spara datan
    filename = f"weather_{CITY}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(weather_data, file, ensure_ascii=False, indent=4)
    
    print(f"Väderdata sparad i filen: {filename}")
except requests.exceptions.RequestException as e:
    print(f"Ett fel uppstod: {e}")
