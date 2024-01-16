from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)


t_colors =  ["red", "blue", "orange", "purple"]
t_names = ["raph", "leo", "mikey", "donnie"]
# turtle_names = [{"name": "", "color":""}]


y_cordinate = [-200, -50, 50, 200]
tmnt = []

race_start = False
start_race = screen.textinput(title="start race", prompt="On your marks, get set ....")

for item in range(4):
        nin_name = t_names[item]
        nin_name = Turtle(shape="turtle")
        nin_name.color(t_colors[item])
        nin_color = t_colors[item]
        nin_name.goto(x=-230, y=y_cordinate[item])
        ninja_profile = dict(name = nin_name, color = nin_color  )
        # tmnt.append(ninja_turtle)
        tmnt.append(ninja_profile)

# print(tmnt)

if start_race == "go":
    race_start = True
    
while race_start:
        for ninja in range(4):
            t_ninja = tmnt[ninja]["name"]
            t_ninja.forward(random.randint(0,10))
            if t_ninja.xcor() > 230:
                   race_start = False
                   winner = t_ninja.pencolor()
                   if winner == "blue":
                        print(f"The winner is Leo")
                   elif winner == "orange":
                        print(f"The winner is Mikey")
                   elif winner == "red":
                        print(f"The winner is Raph")
                   elif winner == "purple":
                        print(f"The winner is Donnie")

screen.exitonclick()