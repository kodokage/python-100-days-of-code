from turtle import Screen
import time
from snake import Snake

screen = Screen()

screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title(titlestring="My Snake Game")
snake_color = screen.textinput(title="Snake color", prompt="Enter snake color")
screen.tracer(0)

snake = Snake(snake_color)

"""Key bindings to direct snake in response to direction keys"""
screen.listen()
screen.onkey(key="Up", fun = snake.up)
screen.onkey(key="Down", fun = snake.down)
screen.onkey(key="Left", fun = snake.left)
screen.onkey(key="Right", fun = snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()




screen.exitonclick()