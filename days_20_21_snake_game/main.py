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
score.show_score(0)
score_counter = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        screen.update()
        score_counter += 1
        score.clear()
        score.show_score(1)
        snake.extend()
        # print(score_counter)

    #Detect collision with wall
        
    if snake.head.xcor() > 240 or snake.head.xcor()<-240 or snake.head.ycor()> 240 or snake.head.ycor()< - 240 :
        game_is_on = False
        score.gameover()

    #Detect Collision with tail
    # If the head collides with any segment in tail  trigger game over
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.gameover()
       




screen.exitonclick()