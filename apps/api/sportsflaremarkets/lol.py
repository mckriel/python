import requests

LEAGUE_MARKETS_ENDPOINT = 'http://docs.sportsflare.io/boy/challenge_definitions_v1_0.json'
GOOGLE_SHEET_ENDPOINT = 'https://api.sheety.co/e5c80948d0c63fe747b73b8127699f62/sportsFlareMarkets/leagueOfLegends'

response = requests.get(url=LEAGUE_MARKETS_ENDPOINT)
result = response.json()
markets = result['definitions']
print(markets)

for key, value in markets.items():
    if len(value['conditions']) == 2:
        attribute2 = value['conditions'][1]['attribute']
        operator2 = value['conditions'][1]['operator']
        value2 = value['conditions'][1]['value']
    else:
        attribute2 = ''
        operator2 = ''
        value2 = ''

    sheet_input = {
        'leagueOfLegend': {
            'name': key,
            'description': value['description'],
            'attributes': len(value['conditions']),
            'attribute1': value['conditions'][0]['attribute'],
            'operator1': value['conditions'][0]['operator'],
            'value1': value['conditions'][0]['value'],
            'attribute2': attribute2,
            'operator2': operator2,
            'value2': value2,
        }
    }

    sheet_response = requests.post(GOOGLE_SHEET_ENDPOINT, json=sheet_input)
    print(sheet_response.text)


