from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")
        self.speed(0)

    def refresh(self):
        ran_x = random.randint(-200, 200)
        ran_y = random.randint(-200, 200)
        self.goto(ran_x, ran_y)



