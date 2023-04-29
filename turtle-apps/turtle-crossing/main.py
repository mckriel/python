import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

timmy = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(timmy.move, 'w')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(timmy) < 20:
            game_is_on = False
            scoreboard.game_over()

    if timmy.is_at_finish():
        timmy.go_to_start()
        car_manager.update_speed()
        scoreboard.increment_level()


screen.exitonclick()
