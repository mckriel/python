from turtle import Turtle, Screen

numbers_list = []
screen = Screen()
tim = Turtle(shape='turtle')
tim.color('coral')


def draw_shape(sides_of_shape):
    angle = round(360 / sides_of_shape)
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


build_sides_array(int(input('Enter number of sides: ')))

for number in numbers_list:
    draw_shape(number)


screen.exitonclick()
