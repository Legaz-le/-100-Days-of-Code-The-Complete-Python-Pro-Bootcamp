from reprlib import recursive_repr
from turtle import Turtle,Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time




screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
score = Scoreboard()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()







screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.fast)
    screen.update()
    ball.move()

    #Collistion with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() <  - 320:
        ball.bounce_x()

    #R_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    #l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()











screen.exitonclick()
