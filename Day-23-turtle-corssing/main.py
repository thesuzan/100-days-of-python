from turtle import Screen
from player import Player
from car import Car
import car_manager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player1 = Player()
car_manager.car_maker()

screen.listen()
screen.onkeypress(player1.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_car()
