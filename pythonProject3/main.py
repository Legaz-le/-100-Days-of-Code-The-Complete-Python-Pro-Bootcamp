from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color:")
color = ["red","orange","yellow","green","blue","purple"]
print(user_bet)
y_positions = [-70,-40,-10,20,50,80]
all_turtles = []

for turtle_index in range(0,6):
     new_turtle = Turtle(shape="turtle")
     new_turtle.penup()
     new_turtle.color(color[turtle_index])
     new_turtle.goto(x=-230, y=y_positions[turtle_index])
     all_turtles.append(new_turtle)

if user_bet:
    is_race_on =True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You've won {wining_color}")
            else:
                print(f"You lost {wining_color}")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)








screen.exitonclick()
