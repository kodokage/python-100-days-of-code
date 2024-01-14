from turtle import Turtle, Screen
import random

shelly = Turtle()
shelly.width(10)
shelly.hideturtle()
shelly.speed("fastest")

colors = ["cornsilk", "orange red", "cyan", "dark orchid", "lawn green", "black"]
angle = [0,90,180,270]

def random_walk(angle):
    shelly.forward(20)
    shelly.right(angle)

for _ in range(2000):
    turn_angle = random.choice(angle)
    shelly.color(random.choice(colors))
    random_walk(turn_angle)






screen = Screen()
screen.exitonclick()