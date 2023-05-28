from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


def main():
    screen = Screen()
    screen.bgcolor('black')
    screen.setup(width=800, height=600)
    screen.title('Paddle')
    screen.tracer(0)

    left_paddle = Paddle((-360, 0))
    right_paddle = Paddle((350, 0))
    ball = Ball()
    score = Score()

    screen.listen()
    screen.onkey(left_paddle.go_up, 'w')
    screen.onkey(left_paddle.go_down, 's')
    screen.onkey(right_paddle.go_up, 'Up')
    screen.onkey(right_paddle.go_down, 'Down')

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        ball.move()

        if ball.ycor() > 275 or ball.ycor() < -275:
            ball.bounce_y()

        if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -335:
            ball.bounce_x()

        if ball.xcor() > 400:
            score.update_score('left')
            ball.reset_ball()
        elif ball.xcor() < -400:
            score.update_score('right')
            ball.reset_ball()

    screen.exitonclick()


main()
