import random
from turtle import Turtle
from random import Random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.generate = 0

    def generate_car(self):
        self.generate += 1
        if self.generate == 6:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)
            self.generate = 0

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def update_speed(self):
        self.car_speed += MOVE_INCREMENT
