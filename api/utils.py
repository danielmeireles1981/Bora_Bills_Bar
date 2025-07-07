import requests

def previsao_tempo(latitude, longitude):
    """
    Busca a previsão do tempo atual pela Open-Meteo API.
    """
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}&current_weather=true&timezone=auto"
    )
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            data = r.json()
            weather = data.get('current_weather', {})
            return weather  # Dict com temperature, weathercode, windspeed, etc
    except Exception as e:
        print(f"Erro ao buscar previsão do tempo: {e}")
    return None

def obter_lat_lon_por_cidade(nome_cidade):
    """
    Usa Open-Meteo Geocoding API para buscar latitude e longitude de uma cidade.
    """
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={nome_cidade}&count=1&language=pt&format=json"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            data = r.json()
            if data.get("results"):
                resultado = data["results"][0]
                return resultado["latitude"], resultado["longitude"]
    except Exception as e:
        print(f"Erro ao buscar lat/lon: {e}")
    return None, None
