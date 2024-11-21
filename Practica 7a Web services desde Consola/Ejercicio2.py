#!/usr/bin/env python3
import requests
import urllib.parse
import http.client
import json

def clima(llave):
    clima = {
        'Thunderstorm': 'Tormenta',
        'Clouds': 'Nublado',
        'Clear': 'Despejado',
        'Haze': 'Neblina',
        'Mist': 'Niebla',
        'Rain': 'Lluvia',
        'Snow': 'Nieve'
    }
    return clima.get(llave, llave)

try:
    # URL de la API
    url = "http://api.openweathermap.org/data/2.5/weather"
    parametros = {
        "id": 3995465,  # ID de Ciudad (v.g: Monterrey, México)
        "units": "metric",
        "APPID": "471b08441f3fb5c7c55fdcdf2cf982e2",
        "lang": "es"
    }
    
    # Realizar solicitud
    response = requests.get(url, params=parametros, timeout=30)
    response.raise_for_status()  # Lanza error si la solicitud falla
    
    # Cargar datos JSON
    djson = response.json()
    
    # Mostrar datos relevantes
    print("Ciudad:", djson['name'])
    print("Coordenadas: Latitud =", djson['coord']['lat'], ", Longitud =", djson['coord']['lon'])
    print("Clima:", clima(djson['weather'][0]['main']))
    print("Descripción:", djson['weather'][0]['description'])
    print("Temperatura actual:", djson['main']['temp'], "°C")
    print("Sensación térmica:", djson['main']['feels_like'], "°C")
    print("Humedad:", djson['main']['humidity'], "%")
    print("Velocidad del viento:", djson['wind']['speed'], "m/s")

except requests.exceptions.RequestException as e:
    print(f"Error al consultar datos: {e}")
