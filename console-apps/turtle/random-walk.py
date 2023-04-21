from turtle import Turtle, Screen
import random

degree = [0, 90, 180, 270]
colour = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

screen = Screen()
timmy = Turtle()
timmy.pensize(8)
timmy.speed(10)


def move():
    timmy.color(random.choice(colour))
    timmy.setheading(random.choice(degree))
    timmy.fd(50)


for _ in range(100):
    move()
