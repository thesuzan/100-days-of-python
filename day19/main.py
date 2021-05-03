from turtle import Turtle, Screen
import random

kachuwa = Turtle()
# kachuwa.pensize(3)
# kachuwa.speed("fastest")

def w_func():
    kachuwa.fd(5)

def s_func():
    kachuwa.bk(5)

def d_func():
    kachuwa.right(15)

def a_func():
    kachuwa.left(15)

def c_func():
    kachuwa.reset()

screen = Screen()
screen.listen()
screen.onkeypress(key="w", fun=w_func)
screen.onkeypress(key="s", fun=s_func)
screen.onkeypress(key="a", fun=a_func)
screen.onkeypress(key="d", fun=d_func)
screen.onkeypress(key="c", fun=c_func)



# def change_color():
#     R = random.randint(0, 255)
#     G = random.randint(0, 255)
#     B = random.randint(0, 255)
#
#     kachuwa.pencolor(R, G, B)


screen.exitonclick()
