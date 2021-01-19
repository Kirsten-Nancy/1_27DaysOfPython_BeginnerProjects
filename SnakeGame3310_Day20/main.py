from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()

screen.title("Snake Game 3310")
screen.bgcolor("thistle")
screen.colormode(255)
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
snake_food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

def draw_border():
    snake_border = Turtle()
    snake_border.penup()
    snake_border.goto(-270, -270)
    snake_border.pendown()
    snake_border.pensize(5)
    for _ in range(4):
        snake_border.fd(540)
        snake_border.left(90)
    snake_border.hideturtle()


game_active = True

def prompt_user():
    continue_game = screen.textinput(title='Do you want to play another game?',
                                     prompt="Enter 'y' to continue 'n' to exit")
    if continue_game == 'y':
        snake.reset()
    else:
        global game_active
        game_active = False


while game_active:
    draw_border()
    screen.update()
    time.sleep(0.04)
    snake.move()

    # Collision with food
    if snake.snake_head.distance(snake_food) <= 15:
        # print("Collision")
        snake_food.food_random_location()
        score_board.increment_score()
        snake.extend_snake()

    # Collision with wall
    if snake.snake_head.xcor() > 260 or snake.snake_head.xcor() < -260 or snake.snake_head.ycor() < -260 or snake.snake_head.ycor() > 260:
        prompt_user()
        score_board.reset_game()

    # Snake head collision with body
    for segment in snake.snake_segments[1:]:
        if snake.snake_head.distance(segment) < 5:
            prompt_user()
            score_board.reset_game()
    # for segment in snake.snake_segments:
    #     if segment == snake.snake_head:
    #         pass
    #     elif snake.snake_head.distance(segment) < 15:
    #         game_score.game_over()

screen.exitonclick()
# TODO: Local persistence, last highest score of player -DONE