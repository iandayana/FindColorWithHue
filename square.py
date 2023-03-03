import random
from turtle import Turtle


class Square(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=10, stretch_len=10)
        self.goto(0, 40)
        self.color_r = 1
        self.color_g = 1
        self.color_b = 1
        self.color(self.color_r, self.color_g, self.color_b)

    def change_color(self):
        self.color_r = random.random()
        self.color_g = random.random()
        self.color_b = random.random()
        self.color(self.color_r, self.color_g, self.color_b)










