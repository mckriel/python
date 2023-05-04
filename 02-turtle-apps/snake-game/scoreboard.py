from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')
FONT_SIZE = 24


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = self.high_score_read()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High score: {self.high_score_read()}', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score_write(self.score)
        self.score = 0
        self.update_scoreboard()

    def high_score_read(self):
        with open('high_score.txt') as file:
            return int(file.read())

    def high_score_write(self, score):
        with open('high_score.txt', mode='w') as file:
            file.write(str(score))
