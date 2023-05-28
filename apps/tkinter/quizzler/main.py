from question_model import Question
from quiz_brain import QuizBrain
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

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
