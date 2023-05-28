import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
screen = Screen()
screen.setup(width=500, height=500)
all_turtles = []


def create_y_coordinate_array(screen_height):
    y_array = []
    position = (screen_height / 2) - (screen_height * 0.04)
    for _ in range(10):
        y_array.append(position)
        position -= screen_height / 10
    return y_array


def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


def create_turtle_y_positions(number_of_turtles, y_coordinate_array):
    if number_of_turtles % 2 != 0 or number_of_turtles > 8 or number_of_turtles < 2:
        print('Input an even number between 2 and 8')

    slice_value = int((10 - number_of_turtles) / 2)

    # slice elements from the front and back of the array
    turtle_y_positions = y_coordinate_array[slice_value:]
    turtle_y_positions = turtle_y_positions[:len(turtle_y_positions) - slice_value]

    return turtle_y_positions


def place_turtles(turtle_starting_positions):
    for turtle_position in turtle_starting_positions:
        new_turtle = Turtle(shape='turtle')
        new_turtle.penup()
        new_turtle.color(generate_random_color())
        new_turtle.goto(x=-230, y=turtle_position)
        all_turtles.append(new_turtle)


def race():
    place_turtles(create_turtle_y_positions(8, create_y_coordinate_array(screen.window_height())))

    user_bet = screen.textinput(title='Make your bet',
                                prompt=f'Which turtle will win the race? Enter a number between 1 and {len(all_turtles)}')
    race_on = True

    while race_on:
        for turtle in all_turtles:
            if turtle.xcor() >= 230:
                race_on = False
                winner = all_turtles.index(turtle) + 1
                print(f'Winner: {winner}')
                if winner == user_bet:
                    print(f"You've won! Turtle number {winner} is the winner!")
                else:
                    print(f"You've won! Turtle number {winner} is the winner!")
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


race()

screen.exitonclick()
