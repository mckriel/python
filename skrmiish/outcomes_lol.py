from urllib.request import urlopen
import json

def retrieve_outcomes():
    url ='http://docs.sportsflare.io/boy/challenge_definitions_v1_0.json'
    response = urlopen(url)
    data = json.loads(response.read())
    data = data['definitions']

    outcome_counter = 1

    for key, value in data.items():
        description = value['description']
        total_attributes = len(value['conditions'])
        print(f'\nOutcome {outcome_counter}: {key.capitalize()}')
        print(f'Definition: {description}')
        print(f'Total attributes: {total_attributes}')
        for item in value['conditions']:
            attribute = item['attribute']
            operator = item['operator']
            value = item['value']
            print(f'\tAttribute: {attribute.capitalize()} is "{operator}" to {value}')
        outcome_counter += 1

retrieve_outcomes()
