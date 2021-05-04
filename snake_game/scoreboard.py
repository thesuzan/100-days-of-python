from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.set_score()

    def set_score(self):
        self.clear()
        self.board_text = "Score: " + str(self.score)
        self.write(self.board_text, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)