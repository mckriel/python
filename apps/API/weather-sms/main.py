import requests
from twilio.rest import Client
import authentication

lat = -33.92
lon = 18.42
url = 'https://api.openweathermap.org/data/3.0/onecall'
params = {
    'lat': lat,
    'lon': lon,
    'appid': authentication.api_key_weather,
}

will_rain = False

response = requests.get(url=url, params=params)
response.raise_for_status()
data = response.json()
weather_hourly = data['hourly'][:12]
for hourly_weather in weather_hourly:
    condition_code = hourly_weather['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(authentication.twilio_account_sid, authentication.twilio_auth_token)
    message = client.messages.create(
        body="It is going to rain today, don't forget an umbrella.",
        from_="+13613103699",
        to="+27796780829"
    )
    print(message.status)
