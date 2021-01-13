from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake_segments = []
        self.colors = ["red", "blue", "white"]
        self.create_snake()

    def create_snake(self):
        # They are three instances
        for i in range(0, 3):
            snake = Turtle(shape="square")
            snake.penup()
            snake.goto(i * -20, 0)
            snake.color(self.colors[i])
            print(snake.pos())
            self.snake_segments.append(snake)

    def move(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            position = self.snake_segments[i - 1].position()
            self.snake_segments[i].goto(position)

        self.snake_segments[0].fd(20)
        # self.snake_segments[0].left(90)

    def up(self):
        self.snake_segments[0].setheading(90)

    def down(self):
        self.snake_segments[0].setheading(270)

    def right(self):
        self.snake_segments[0].setheading(0)

    def left(self):
        self.snake_segments[0].setheading(180)
