import requests

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# data = response.json()
#
# print(f'Latitude: {data["iss_position"]["latitude"]}')
# print(f'Longitude: {data["iss_position"]["longitude"]}')

parameters = {
    'lat': 51.507351,
    'lon': -0.127758,
    'date': '2023-05-28'
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
print(response)
response.raise_for_status()
data = response.json()
print(data)
