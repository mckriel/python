import requests
from datetime import datetime

PIXELA_URL = 'https://pixe.la/v1/users'
USERNAME = 'mckriel'
TOKEN = 'Mk871029'
HEADERS = {
         'X-USER-TOKEN': TOKEN
     }
GRAPH_ID = 'graph1'

def create_user(url):
    params = {
        'token': TOKEN,
        'username': USERNAME,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes'
    }
    response = requests.post(url=url, json=params)
    print(response.text)


def create_graph(name, url, token):
    graph_endpoint = f'{url}/{USERNAME}/graphs'
    params = {
         'id': 'graph1',
         'name': name,
         'unit': 'pages',
         'type': 'int',
         'color': 'momiji',
    }
    response = requests.post(url=graph_endpoint, json=params, headers=HEADERS)
    print(response.text)


def log_pixel(url, value):
    today = datetime.now()
    print(today.strftime('%Y%m%d'))
    pixel_endpoint = f'{url}/{USERNAME}/graphs/{GRAPH_ID}'
    pixel_data = {
        'date': today.strftime('%Y%m%d'),
        'quantity': value,
    }
    response = requests.post(pixel_endpoint, json=pixel_data, headers=HEADERS)
    print(response.text)


# RUN ORDER
# create_user(PIXELA_URL)
# create_graph('Reading Tracker', PIXELA_URL, TOKEN)
# log_pixel(PIXELA_URL, '35')
