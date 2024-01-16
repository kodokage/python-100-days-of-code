from turtle import Turtle, Screen


tim = Turtle()

def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def right_turn():
    tim.right(10)

def left_turn():
    tim.left(10)


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=right_turn)
screen.onkey(key="d", fun=left_turn)
screen.onkey(key="c", fun=tim.reset)


screen.exitonclick()