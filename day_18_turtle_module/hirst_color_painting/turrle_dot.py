from turtle import Turtle, Screen
import random


mikey = Turtle()
mikey.penup()
mikey.setheading(225)
mikey.forward(250)
mikey.setheading(0)
# mikey.colormode(255)
number_of_dots = 100

color_list = ["cornsilk", "orange red", "cyan", "dark orchid", "lawn green", "black"]

for dot_count in range(number_of_dots):
    mikey.dot(20, random.choice(color_list))
    mikey.forward(50)
    if dot_count % 10 == 0:
        mikey.setheading(90)
        mikey.forward(50)
        mikey.setheading(180)
        mikey.forward(500)
        mikey.setheading(10)



screen = Screen()
screen.exitonclick()

