from turtle import Turtle, Screen
import random

kachuwa = Turtle()
# kachuwa.pensize()
kachuwa.speed(25)

screen = Screen()
screen.colormode(255)

def change_color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    kachuwa.pencolor(R, G, B)


for i in range(0, 370, 5):
    kachuwa.circle(100)
    kachuwa.seth(i)
    change_color()

screen.exitonclick()
