from turtle import Turtle, Screen
import random

kachuwa = Turtle()
kachuwa.pensize(3)
kachuwa.speed("fastest")

angles = [0, 90, 180, 270]
screen = Screen()


def change_color():
    R = random.randint(0, screen.colormode())
    G = random.randint(0, screen.colormode())
    B = random.randint(0, screen.colormode())

    kachuwa.pencolor(R, G, B)


for i in range(1000):
    angle = random.choice(angles)
    kachuwa.right(angle)
    kachuwa.forward(10)
    change_color()


screen.exitonclick()
