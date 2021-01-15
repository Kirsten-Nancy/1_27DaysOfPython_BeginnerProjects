from turtle import Turtle
import random

# food is a turtle object that inherits all features from Turtle class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(0)
        self.penup()
        self.shapesize(stretch_wid=0.3, stretch_len=0.3)
        self.food_random_location()

    def food_random_location(self):
        x_pos = random.randint(-255, 255)
        y_pos = random.randint(-255, 255)
        self.goto(x_pos, y_pos)

