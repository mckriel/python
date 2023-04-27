from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)

        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1
        print(self.x_move)

    def bounce_y(self):
        self.y_move *= -1
        print(self.y_move)

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_x()
