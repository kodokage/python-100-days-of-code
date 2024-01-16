from turtle import Turtle, Screen

raph = Turtle()
screen = Screen()

def move_forwards():
    raph.forward(10)

def right_turn():
    raph.right(90)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(right_turn, "r")



screen.exitonclick()