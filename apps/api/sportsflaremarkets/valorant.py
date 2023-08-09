import requests

VALORANT_MARKETS_ENDPOINT = 'https://file.notion.so/f/s/10bb404a-25b2-4347-beca-46569be6bc50/challenge_definitions_valorant_v1.json?id=01c3ac6f-74aa-4ca8-a476-7342c32b632b&table=block&spaceId=e8db23f9-964e-4297-8744-a2979d239a32&expirationTimestamp=1691668800000&signature=cC-wb2ElcujxbOGGGkzw_TcGOkuLmY1lc0MdmH3DrMY&downloadName=challenge_definitions_valorant_v1.json'
GOOGLE_SHEET_ENDPOINT = 'https://api.sheety.co/e5c80948d0c63fe747b73b8127699f62/sportsFlareMarkets/valorant'

response = requests.get(url=VALORANT_MARKETS_ENDPOINT)
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
        'valorant': {
            'name': key,
            'description': value['description'],
            'attribute': value['conditions'][0]['attribute'],
            'operator': value['conditions'][0]['operator'],
            'value': value['conditions'][0]['value'],
        }
    }

    sheet_response = requests.post(GOOGLE_SHEET_ENDPOINT, json=sheet_input)
    print(sheet_response.text)
