import requests
import json
from datetime import datetime
from urllib.parse import urlparse, urlencode

def getweather_data(api_key, city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    url_with_params = f"{base_url}?{urlencode(params)}"

    result = requests.get(url_with_params)

    endpoint = urlparse(base_url).path
    endpoint = endpoint.replace("/", "")

    now = datetime.now()
    date_time = now.strftime("%Y%m%d%H%M%S")

    payload = {
        'data': result.json(),
        'date': date_time,
        'endpoint': endpoint
    }

    filename = f"{city_name}_{endpoint}_{date_time}.json"
    with open(filename, "w") as outfile:
        json.dump(payload, outfile)

api_key = "288b9c5427f321582c5aa307d299cbc6"
city_name = "Paris"

getweather_data(api_key, city_name)
