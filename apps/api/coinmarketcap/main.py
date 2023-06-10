from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

API_KEY = '070c6809-7428-4ae4-82c8-50801d1dc6de'


def crypto_latest_listings(return_limit):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': str(return_limit),
        'convert': 'ZAR',

    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY
    }
    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url=url, params=parameters)
        data = response.json()

        if data['status']['error_code'] != 0:
            print(f"Error code: {data['status']['error_code']}, Error message: {data['status']['error_message']}")
        rank = 0
        for coin in data['data']:
            rank += 1
            name = coin['name']
            price = "{:,.2f}".format(round(float(coin['quote']['ZAR']['price']), 2))
            print(f"{rank}: {name}, Price: R{price}")
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


crypto_latest_listings(10)
