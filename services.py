import os
from datetime import datetime, timezone
from typing import Tuple
import requests


API_KEY = os.environ.get('API_KEY')
API_URL = "https://api.openweathermap.org/data/2.5/air_pollution"
GEOCODE_URL = "http://api.openweathermap.org/geo/1.0/direct"


def get_coords_by_city_name(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'limit': 1
    }
    r = requests.get(GEOCODE_URL, params=params)
    
    if r.status_code == 200 and r.json():
        lat = r.json()[0]['lat']
        lon = r.json()[0]['lon']
        return (lat, lon)
    else:
        return None


def get_air_quality_data(location: str | Tuple[float, float]):
    if isinstance(location, str):
        coordinates = get_coords_by_city_name(location)
        if coordinates is None:
            return None
    else:
        coordinates = location

    params = {
        "lat": coordinates[0],
        "lon": coordinates[1],
        "appid": API_KEY,
    }

    r = requests.get(API_URL, params=params)

    if r.status_code == 200:
        data = r.json()
        return data
    else:
        return None


def format_last_updated(timestamp):
    dt_utc = datetime.fromtimestamp(timestamp, timezone.utc)
    return dt_utc.strftime('%Y-%m-%d %H:%M:%S')
