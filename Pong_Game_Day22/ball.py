from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        print(self)
        super(Ball, self).__init__()
        print(self)
        self.penup()
        self.shape('circle')
        self.color('white')
        self.x_move = 20
        self.y_move = 20
        self.move_speed = 0.1

    def move(self):
        # self.setheading(45)
        # self.fd(30)
        # Allow changes to other directions
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)
        print(y_pos, x_pos)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()