from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')
FONT_SIZE = 24


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.left_paddle_score = 0
        self.right_paddle_score = 0

        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Left: {self.left_paddle_score} Right: {self.right_paddle_score}', align=ALIGNMENT, font=FONT)

    def update_score(self, paddle):
        if paddle == 'left':
            self.left_paddle_score += 1
            self.clear()
            self.update_scoreboard()
        else:
            self.right_paddle_score += 1
            self.clear()
            self.update_scoreboard()
