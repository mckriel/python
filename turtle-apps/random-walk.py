import turtle as t
import random

degree = [0, 90, 180, 270]

t.colormode(255)
timmy = t.Turtle()
timmy.pensize(8)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour_tuple = (r, g, b)
    return colour_tuple


def move():
    timmy.color(random_colour())
    timmy.setheading(random.choice(degree))
    timmy.fd(50)


for _ in range(100):
    move()
