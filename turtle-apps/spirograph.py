import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed('fastest')


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


def draw_spirograph_method_1(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


def draw_spirograph_method_2(number_of_circles):
    for _ in range(number_of_circles):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + 360/number_of_circles)
        print(tim.heading())


# Uncomment to draw
# draw_spirograph_method_1(5) # Input the gap between circles in degrees
# draw_spirograph_method_2(100) # Input the total amount of cirlces to draw


screen = t.Screen()
screen.exitonclick()