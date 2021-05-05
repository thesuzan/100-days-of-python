from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 3

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1


        # incidence = self.heading()

        # if (incidence % 180) < 180:
        #     quadrant = int(incidence / 45)
        #     d_angle = (quadrant * 45) - incidence
        #     reflection = incidence + d_angle * 2
        #     self.setheading(reflection)
        # else:
        #     quadrant = int(incidence / 45)
        #     d_angle = (quadrant * 45) + incidence
        #     reflection = incidence + d_angle * 2
        #     self.setheading(reflection)
