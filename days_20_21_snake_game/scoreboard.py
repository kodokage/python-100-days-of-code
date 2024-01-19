from turtle import Turtle
FONT = font= ("Tahoma", 14, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.clear()
        self.goto(x=0, y=210)

    def show_score(self, value):
        self.score += value
        self.write("Your Score : " + str(self.score), False, align="center", font= FONT)
        
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
 
        