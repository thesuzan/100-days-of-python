from turtle import Turtle, Screen
import random

kachuwa = Turtle()

sides = [3, 4, 5, 6, 7, 8, 9, 10]

kachuwa.pensize(5)

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()

    kachuwa.pencolor(R, G, B)


for side in range(3,100):
    angle = 360 / side
    for _ in range(side):
        kachuwa.forward(100)
        kachuwa.right(angle)
    change_color()

screen = Screen()

screen.exitonclick()
