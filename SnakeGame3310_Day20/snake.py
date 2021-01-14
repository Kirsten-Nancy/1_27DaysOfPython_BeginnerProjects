from turtle import Turtle

# Sake class has several turtles
class Snake:
    def __init__(self):
        self.snake_segments = []
        self.colors = ["red", "blue", "white"]
        self.create_snake()
        self.snake_head = self.snake_segments[0]

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

        self.snake_head.fd(20)

    # The conditional checks to prevent the snake from moving in both directions
    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)
