import requests
from datetime import datetime

GENDER = 'male'
WEIGHT_KG = 85
HEIGHT_CM = 182
AGE = 35

APP_ID = '41c4bcf7'
API_KEY = '6cb8ce184581dc82d3c9ba9b3dae5976'

EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT = 'https://api.sheety.co/e5c80948d0c63fe747b73b8127699f62/myWorkouts/workouts'

HEADERS = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

exercise_text = input('What exercise did you do?')
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=HEADERS)
result = response.json()

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

for exercise in result['exercises']:
    sheet_input = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }

sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_input)
print(sheet_response.text)