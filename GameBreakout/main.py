from turtle import *
from boxes import Boxes
from ball import Ball
from scoreboard import Scoreboard
import time


screen= Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Breakout Game")
screen.tracer(0)

boxes = Boxes()
ball = Ball()
boxes.get_on_line()
score = Scoreboard()

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1,stretch_len=8)
paddle.penup()
paddle.goto(0,-240)

def go_left():
    new_x = paddle.xcor() - 20
    paddle.goto(new_x,paddle.ycor())
def go_right():
    new_x = paddle.xcor() + 20
    paddle.goto(new_x,paddle.ycor())

screen.listen()
screen.onkeypress(go_left,"Left")
screen.onkeypress(go_right,"Right")

game_is_on = True
life = 5
print("You have only 5 lives")
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280:
        ball.bounce_y()
    elif ball.xcor() > 370 or ball.xcor() < -370:
        ball.bounce_wall()


    if ball.distance(paddle) < 50 and ball.ycor() < -220:
        ball.bounce_y()

    for box in boxes.all_boxes:
        if ball.distance(box) < 50:  # Adjust threshold based on box/ball size
            # Calculate collision direction
            ball_x, ball_y = ball.pos()
            box_x, box_y = box.pos()
            dx = abs(ball_x - box_x)
            dy = abs(ball_y - box_y)

            # Vertical collision (top/bottom)
            if dy > dx:
                ball.bounce_y()
            # Horizontal collision (sides)
            else:
                ball.bounce_wall()

            # Remove/hide the hit box
            box.hideturtle()
            boxes.all_boxes.remove(box)
            time.sleep(ball.move_speed)
            score.point()# Remove the box from the list
            break  # Exit the loop after handling one collision

    if ball.ycor()  < - 280:
        ball.reset_position()
        life = -1
        if life == 0:
            print(f"current{life}")
        else:
            game_is_on = False
screen.exitonclick()