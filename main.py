from turtle import Screen
from paddles import Paddle
from Ball import Ball
from scoreboard import Scoreboard
import time
from math import fabs

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()
ball = Ball()
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')

screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() <= -280 or ball.ycor() >= 280:
        ball.collision_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.collision_x()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_get_point()
        ball.increase_speed()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_get_point()
        ball.increase_speed()

    if scoreboard.l_score == 1:
        game_is_on = False
        scoreboard.winner()

screen.exitonclick()




