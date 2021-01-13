from turtle import Screen
import time
from snake import Snake

screen = Screen()

screen.title("Snake Game 3310")
screen.bgcolor("DarkSlateGrey")
screen.colormode(255)
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_active = True
while game_active:
    time.sleep(0.1)
    screen.update()
    snake.move()

screen.exitonclick()
