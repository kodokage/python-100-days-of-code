from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0), (-40,0)]

class Snake():
    def __init__(self, s_color):
        self.s_color = s_color
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    """method creates snake segments and adds them to the segments list"""
    def create_snake(self):

        for positon in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color(self.s_color)
            new_segment.penup()
            new_segment.goto(positon)
            self.segments.append(new_segment)

    """Move method makes snake segments move in sequence"""
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -2].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    """Set headings to direct snake motion"""

    def up(self):
        for seg_num in self.segments:
            seg_num.setheading(90)

    def down(self):
        for seg_num in self.segments:
            seg_num.setheading(270)

    def right(self):
        for seg_num in self.segments:
            seg_num.setheading(0)

    def left(self):
        for seg_num in self.segments:
            seg_num.setheading(180)
