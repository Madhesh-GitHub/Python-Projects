from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scorecard import ScoreCard
import time



screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = ScoreCard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50     and ball.xcor() >320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    #detect R paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
        ball.bounce_x()

    #detect L paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()
        ball.bounce_y()





screen.exitonclick()
