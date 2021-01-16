from turtle import Screen
from player_paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title('Pong Game')
screen.bgcolor('black')
screen.tracer(0)

screen.listen()
# Passing in the different coordinate tuple of the paddles and color when creating the paddle objects
left_paddle = Paddle((-350, 0), 'plum')
right_paddle = Paddle((350, 0), 'LightSkyBlue')

# Ball creation
ball = Ball()

scoreboard = ScoreBoard()

# Moving the paddles
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')

game_is_active = True

while game_is_active:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # If right player misses the ball
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.increase_left_score()

    # If left player misses the ball
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.increase_right_score()

screen.exitonclick()