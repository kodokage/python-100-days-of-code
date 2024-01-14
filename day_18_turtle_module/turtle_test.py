from turtle import Turtle, Screen
from random import choice

tim = Turtle()

tim.shape("turtle")
tim.color("blue")

# for _ in range(4):
#     for _ in range(4):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()
#     tim.right(90)




colors = ["red", "blue", "yellow", "black"]

def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):  
        tim.forward(100)
        tim.right(angle)


for side in range(3,11):
    tim.color(choice(colors))
    draw_shape(side)
  

    
    



screen = Screen()
screen.exitonclick()