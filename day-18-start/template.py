from turtle import Turtle, Screen
import random

kachuwa = Turtle()
kachuwa.pensize(3)
kachuwa.speed("fastest")

screen = Screen()


def change_color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    kachuwa.pencolor(R, G, B)


screen.exitonclick()
