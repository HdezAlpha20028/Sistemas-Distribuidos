import requests
import urllib.parse
import http.client
import json

def climaEs(llave):
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

def climaName(ubicacion, api_key):

    url = "http://api.openweathermap.org/data/2.5/weather"
    parametros = {
        "q": ubicacion,  # Ciudad
        "units": "metric",
        "appid": api_key,
        "lang": "es"
    }
    
    try:
        response = requests.get(url, params=parametros, timeout=30)
        response.raise_for_status()
        data = response.json()
        return {
            "ciudad": data['name'],
            "lat": data['coord']['lat'],
            "lon": data['coord']['lon'],
            "clima": climaEs(data['weather'][0]['main']),
            "descripcion": data['weather'][0]['description'],
            "temperatura": data['main']['temp'],
            "sensacion_termica": data['main']['feels_like'],
            "humedad": data['main']['humidity'],
            "viento": data['wind']['speed']
        }
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar OpenWeatherMap: {e}")
        return None

def geonames(lugar, username):
    
    url = "http://api.geonames.org/wikipediaSearchJSON"
    params = {
        "q": lugar,         # Nombre de la ubicación
        "maxRows": 3,       # Número de resultados
        "username": username  # Nombre de username de Geonames --> enriquehdez
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if "geonames" in data and len(data["geonames"]) > 0:
            lugar_info = data["geonames"][0]
            return {
                "nombre": lugar_info.get("title", "N/A"),
                "Summary": lugar_info.get("summary", "N/A"),
                "pais": lugar_info.get("country", "N/A"),
                "poblacion": lugar_info.get("population", "N/A"),
                "lat": lugar_info.get("lat", "N/A"),
                "lng": lugar_info.get("lng", "N/A")
            }
        else:
            print(f"No se encontró información para la ubicación: {lugar}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar Geonames: {e}")
        return None

# API's
openweatherApiK = "471b08441f3fb5c7c55fdcdf2cf982e2"  # API Key de OpenWeatherMap
geonameUser = "enriquehr"  # Usuario de Geonames

# Entrada del usuario
ubicacion = input("Ingresa el nombre de la ciudad que deseé: ").strip()

# Obtener datos del clima desde OpenWeatherMap
climaInfo = climaName(ubicacion, openweatherApiK)
if climaInfo:
    print(f"\nDatos del clima para {climaInfo['ciudad']}:")
    print(f"  Coordenadas: Latitud = {climaInfo['lat']}, Longitud = {climaInfo['lon']}")
    print(f"  Clima: {climaInfo['clima']}")
    print(f"  Descripción: {climaInfo['descripcion']}")
    print(f"  Temperatura: {climaInfo['temperatura']} °C")
    print(f"  Sensación térmica: {climaInfo['sensacion_termica']} °C")
    print(f"  Humedad: {climaInfo['humedad']}%")
    print(f"  Viento: {climaInfo['viento']} m/s")
    
    #  Usar el nombre de la ciudad como entrada para Geonames
    geonamesInfo = geonames(climaInfo['ciudad'], geonameUser)
    if geonamesInfo:
        print(f"\nInformación sobre {geonamesInfo['nombre']} usando Wikipedia Webservice:")
        print(f"  Summary: {geonamesInfo['Summary']}")
        print(f"  País: {geonamesInfo['pais']}")
        print(f"  Población: {geonamesInfo['poblacion']}")
        print(f"  Latitud: {geonamesInfo['lat']}")
        print(f"  Longitud: {geonamesInfo['lng']}")
