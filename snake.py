from turtle import Turtle

XY_VALUES = [(0, 0), (-20, 0),(-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []

    def create_body(self):
        for i in XY_VALUES:
            self.addsnake(i)

    def move_snake(self):
        for i in range(len(self.segment) - 1, 0, -1):
            xval = self.segment[i - 1].xcor()
            ycor = self.segment[i - 1].ycor()
            self.segment[i].goto(xval, ycor)
        self.segment[0].forward(20)

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)

    def addsnake(self, position):
        seg1 = Turtle('square')
        seg1.penup()
        seg1.color('white')
        seg1.goto(position)
        self.segment.append(seg1)
    def extend(self):
        self.addsnake(self.segment[-1].position())
