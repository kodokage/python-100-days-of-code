from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Enter winner color")
# print(user_bet)

# leo = Turtle(shape="turtle")
# leo.color("blue")
# donnie = Turtle(shape="turtle")
# donnie.color("purple")
# raph = Turtle(shape="turtle")
# raph.color("red")
# mikey = Turtle(shape="turtle")
# mikey.color("orange")
# leo.penup()
# donnie.penup()
# raph.penup()
# mikey.penup()

# leo.goto(x=-233, y=170)
# donnie.goto(x=-233, y=50)
# mikey.goto(x=-233, y=-50)
# raph.goto(x=-233, y=-170)

is_race_on = False
y_positon = [-170,-50 ,50 ,170 ] 
colors = ["blue", "purple", "red", "orange"]
all_turtles = []

for turtle_index in range(4):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-230, y= y_positon[turtle_index])
    tim.color(colors[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            winning_color = turtle.pencolor()
            is_race_on = False
            
            if winning_color == user_bet:
                print(f"You won. {winning_color} won")
            else:
                print(f"You lost. {winning_color} won")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()