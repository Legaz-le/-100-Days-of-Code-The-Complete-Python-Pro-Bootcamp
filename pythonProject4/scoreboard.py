from turtle import Turtle
Alignment = "center"
font =("Arial", 20, "normal")




class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
           self.high_score =  int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Your score is {self.score} High score is {self.high_score}", align=Alignment, font=font)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()





    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAMER OVER", align=Alignment, font=font)


    def increase_score(self):
        self.score +=1
        self.update_score()

