from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setx(xcor)

    def up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)
