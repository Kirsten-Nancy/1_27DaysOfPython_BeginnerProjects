from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()

screen.title("Snake Game 3310")
screen.bgcolor("DarkSlateGrey")
screen.colormode(255)
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
snake_food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_active = True
while game_active:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # If the distance between the two is less than this, the snake has eaten
    if snake.snake_head.distance(snake_food) <= 15:
        print("Collision")
        snake_food.food_random_location()

screen.exitonclick()
