from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import ScoreBoard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
new_ball = Ball()
score_board = ScoreBoard()



screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.go_up)
screen.onkeypress(key="Down", fun=r_paddle.go_down)

screen.onkeypress(key="w", fun=l_paddle.go_up)
screen.onkeypress(key="s", fun=l_paddle.go_down)

game_is_on = True
while game_is_on:
    time.sleep(new_ball.move_speed)
    screen.update()
    new_ball.move()

    ## Detect Collision with wall
    if new_ball.ycor() >= 290 or new_ball.ycor() <= -290:
        new_ball.bounce_y()

    ## Detect collision with right paddle
    if new_ball.distance(r_paddle) < 50 and new_ball.xcor()> 320 or new_ball.distance(l_paddle) < 50 and new_ball.xcor()  < -320:
        new_ball.bounce_x()

    ## Detect if ball goes out of bounds right
    if new_ball.xcor() > 400 :
        new_ball.reset_postion()
        score_board.l_point()

    ## Detect if goes out of bounds left
    if  new_ball.xcor() < -450 :
        new_ball.reset_postion()
        score_board.r_point()

       
screen.exitonclick()