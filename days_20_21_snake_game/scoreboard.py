from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = "High Score"
        self.color("white")
        self.clear()
        self.show_score()
        self.setposition(x=0, y=230)

    def show_score(self):
        
        self.write(self.score, False, align="center")