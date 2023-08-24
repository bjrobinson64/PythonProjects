from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")


screen.update()

is_on = True
while is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    if ball.ycor() > 285 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.xcor() > 330 and r_paddle.distance(ball) < 50) or (
            ball.xcor() < -330 and l_paddle.distance(ball) < 50):
        ball.bounce_x()

    if ball.xcor() > 400:
        scoreboard.left_score()
        ball.reset_ball()
        screen.update()
        time.sleep(2)
    if ball.xcor() < -400:
        scoreboard.right_score()
        ball.reset_ball()
        screen.update()
        time.sleep(2)































screen.exitonclick()
