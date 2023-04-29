from turtle import Turtle, Screen
import random

numbers_list = []
colors = ['ForestGreen', 'MediumBlue', 'DarkRed', 'SlateBlue', 'DarkOrange', 'SaddleBrown', 'Black', 'MediumVioletRed']
screen = Screen()
tim = Turtle(shape='turtle')


def draw_shape(sides_of_shape):
    angle = round(360 / sides_of_shape)
    tim.color(random.choice(colors))
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

# Tab out of the Screen instance and input a number of sides into the console.
build_sides_array(int(input('Enter number of sides: ')))

for number in numbers_list:
    draw_shape(number)


screen.exitonclick()
