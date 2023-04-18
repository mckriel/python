import turtle
from turtle import Turtle, Screen

tim = Turtle(shape='turtle', visible=False)
screen = Screen()
numbers_list = []


def initialize_turtle():

    tim.color('coral')

    TURTLE_SIZE = 20

    tim.penup()
    tim.goto(0.50, screen.window_height() / 2 - TURTLE_SIZE / 2)
    tim.pendown()
    tim.showturtle()


def calculate_angle(number_of_sides):
    return round(360 / number_of_sides)


def draw_shape(sides_of_shape, angle):
    for i in range(sides_of_shape):
        tim.forward(100)
        tim.right(angle)


def build_sides_array(number_of_sides):
    for i in range(number_of_sides):
        array_number = i + 1
        if array_number == 1 or array_number == 2:
            continue

        if (360 % array_number) == 0:
            numbers_list.append(array_number)

    print(numbers_list)


initialize_turtle()

build_sides_array(int(input('Enter number of sides: ')))

for number in numbers_list:
    draw_shape(number, calculate_angle(number))


screen.exitonclick()
