from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(.5, .5)
        self.color("red")
        self.speed("fastest")
        self.respawn()
        self.colors = ["cyan", "purple", "white", "blue","red","orange",'green',"yellow"]

    def respawn(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def changecolor(self):
        self.color(random.choice(self.colors))
