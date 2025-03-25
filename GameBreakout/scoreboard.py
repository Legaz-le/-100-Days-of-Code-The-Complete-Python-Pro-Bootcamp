from turtle import *


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(0, 230)
        self.write(self.score, align="center", font=("Courier", 40, "normal"))
    def point(self):
        self.score += 20
        self.update_score()