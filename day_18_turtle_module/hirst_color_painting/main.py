import colorgram
from turtle import Turtle, Screen
import random

"""Extract colors from images"""
# colors = colorgram.extract('image.jpg', 30)
colors = ["cornsilk", "orange red", "cyan", "dark orchid", "lawn green", "black"]

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)


angle = [0,90,180,270]
donnie = Turtle()
donnie.width(10)
donnie.dot()

def one_line():
    for _ in range(5):
        donnie.color(random.choice(colors))
        donnie.forward(10)
        donnie.penup()
        donnie.forward(10)
        donnie.pendown()

for _ in range(1):
    one_line()
    donnie.left(90)
    donnie.forward(20)
    donnie.left(90)
    one_line()
    donnie.right(90)
    donnie.forward(20)
    donnie.right(90)
    one_line()
    donnie.left(90)
    donnie.forward(20)
    donnie.left(90)
    one_line()
    donnie.right(90)
    donnie.forward(20)
    donnie.right(90)
    one_line()

   
    


screen = Screen()
screen.exitonclick()

