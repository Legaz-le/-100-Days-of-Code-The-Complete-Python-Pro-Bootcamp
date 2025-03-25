import turtle
from turtle import Turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
correct_answer = []

while len(correct_answer) < 50:
    answer_state = screen.textinput(title= f"{len(correct_answer)}/50 States Correct", prompt= "What's another state's name?").title()


    if answer_state == "Exit":
        missing_states = [state for state in states if state not in correct_answer ]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_lear.csv")
        break


    if answer_state in states:
        correct_answer.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)











