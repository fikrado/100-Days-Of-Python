import requests

api_key = "1a574cba6c46aef984b2efbe3061b147"
url = "http://api.openweathermap.org/data/2.5/onecall"

weather = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key
}

r = requests.get(url, params=weather)
r.raise_for_status()
data = r.json()
print(data["hourly"][0]["weather"][0])