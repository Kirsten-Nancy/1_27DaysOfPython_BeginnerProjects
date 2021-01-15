from turtle import Turtle

SNAKE_START_POSITIONS = [(0.00, 0.00), (-10.00, 0.00), (-20.00, 0.00)]

# Snake class has several turtles
class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        # snake positions
        for position in SNAKE_START_POSITIONS:
            self.add_snake_segment(position)

    def add_snake_segment(self, new_pos):
        snake = Turtle(shape="square")
        snake.shapesize(stretch_len=0.5, stretch_wid=0.5)
        snake.penup()
        snake.goto(new_pos)
        snake.color('white')
        print(snake.pos())
        self.snake_segments.append(snake)

    def extend_snake(self):
        self.add_snake_segment(self.snake_segments[-1].position())

    def move(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            position = self.snake_segments[i - 1].position()
            self.snake_segments[i].goto(position)

        self.snake_head.fd(10)

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
