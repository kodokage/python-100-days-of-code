from turtle import Turtle, Screen
import random

leo = Turtle()
#leo.shape("turtle")
leo.speed("fastest")
leo.width(5)
#leo.colornode(255)



def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

for _ in range(50):
    leo.color("orange")
    leo.circle(100)
    leo.setheading(leo.heading()+10)

screen = Screen()
screen.exitonclick()