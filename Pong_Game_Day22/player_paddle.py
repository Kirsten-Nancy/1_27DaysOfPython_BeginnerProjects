from turtle import Turtle

# Paddle is a Turtle relationship
class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape('square')
        self.penup()
        # width= height??
        self.speed(0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(color)
        self.move_paddle(position)

    def move_paddle(self, pos):
        """Takes in the paddle position in form of a tuple"""
        self.goto(pos)

    def up(self):
        """Moves the paddle up by 20 paces"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        """Moves the paddle down by 20 paces"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
