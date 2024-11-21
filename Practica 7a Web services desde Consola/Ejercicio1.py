import requests
import urllib.parse
import http.client
import json

def ObtenerInfo(place, username):
    # URL base del servicio
    url = "http://api.geonames.org/wikipediaSearchJSON"
    
    # Parámetros de la solicitud
    params = {
        "q": place,         # Nombre de la ubicación
        "maxRows": 3,       # Número de resultados (1 para el más relevante)
        "username": username  # Nombre de username de Geonames
    }
    
    try:
        # Realizar solicitud a la API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Lanza error si la solicitud falla
        
        # Procesar respuesta JSON
        data = response.json()
        if "geonames" in data and len(data["geonames"]) > 0:
            lugar_info = data["geonames"][0]
            print(f"Nombre: {lugar_info.get('title', 'N/A')}")
            print(f"Resumen: {lugar_info.get('summary', 'N/A')}")
            print(f"País: {lugar_info.get('country', 'N/A')}")
            print(f"Población (aproximada): {lugar_info.get('population', 'N/A')}")
            print(f"Latitud: {lugar_info.get('lat', 'N/A')}")
            print(f"Longitud: {lugar_info.get('lng', 'N/A')}")
        else:
            print(f"No se encontró información para la ubicación: {place}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")

# Nombre de la ubicación a buscar
ubicacion = "Cordova"

# Usuario de Geonames
username = "enriquehr"  

# Llamar a la función
ObtenerInfo(ubicacion, username)

#PRUEBA DE FUNCIONAMIENTO:

# http://api.geonames.org/wikipediaSearchJSON?q=Cordova&maxRows=3&username=enriquehr