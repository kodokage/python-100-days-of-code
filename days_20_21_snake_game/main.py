from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import ScoreBoard

screen = Screen()

screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title(titlestring="My Snake Game")
snake_color = screen.textinput(title="Snake color", prompt="Enter snake color")
screen.tracer(0)

snake = Snake(snake_color)
food = Food()

"""Key bindings to direct snake in response to direction keys"""
screen.listen()
screen.onkey(key="Up", fun = snake.up)
screen.onkey(key="Down", fun = snake.down)
screen.onkey(key="Left", fun = snake.left)
screen.onkey(key="Right", fun = snake.right)

game_is_on = True
score = ScoreBoard()
score.show_score()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
#Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()




screen.exitonclick()