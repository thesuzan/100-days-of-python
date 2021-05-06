from turtle import Turtle
import random

COLORS = ["black", "blue", "green", "pink", "red", "orange", "beige", "bisque", "coral", "cyan", "gray"]
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(180)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        selected_color = random.choice(COLORS)
        self.color(selected_color)

    def move
