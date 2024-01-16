from turtle import Turtle, Screen
import random

# screen = Screen()
# screen.setup(width=500, height=500)


t_colors =  ["red", "blue", "orange", "purple"]
t_names = ["raph", "leo", "mikey", "donnie"]
# turtle_names = [{"name": "", "color":""}]


y_cordinate = [-200, -50, 50, 200]
tmnt = []

# race_start = False
# start_race = screen.textinput(title="start race", prompt="On your marks, get set ....")

for item in range(4):
        nin_name = t_names[item]
        nin_name = Turtle(shape="turtle")
        nin_name.color(t_colors[item])
        nin_color = t_colors[item]
        # nin_name.goto(x=-230, y=y_cordinate[item])
        ninja_profile = dict(name = nin_name, color = nin_color  )
        # tmnt.append(ninja_turtle)
        tmnt.append(ninja_profile)

test_obj = tmnt[1]["name"]

test_obj.forward(50)
