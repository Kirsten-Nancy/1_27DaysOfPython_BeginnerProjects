from turtle import Turtle

class CustomTurtle(Turtle):
    def __init__(self, name):
        super().__init__()
        self.name = name