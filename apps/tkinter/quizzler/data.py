import requests

QUESTION_API_URL = 'https://opentdb.com/api.php'
QUESTION_PARAMETERS = {
    'amount': 10,
    'type': 'boolean'
}


def get_questions():
    response = requests.get(url=QUESTION_API_URL, params=QUESTION_PARAMETERS)
    response.raise_for_status()
    data = response.json()
    return data['results']


question_data = get_questions()
