from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')
FONT_SIZE = 24


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
