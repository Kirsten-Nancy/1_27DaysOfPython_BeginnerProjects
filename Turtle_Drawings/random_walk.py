from turtle import Turtle, Screen
from colors import color_data
import random

DIRECTIONS = [0, 45, 90, 135, 180, 225, 270, 315]

turtle1 = Turtle()
screen = Screen()
screen.setup(width=1000, height=1000)
screen.colormode(255)
screen.title('Random Walk')
turtle1.hideturtle()
turtle1.pensize(15)
turtle1.speed(10)

screen.listen()

walk = True

def stop_game():
    global walk
    walk = False


while walk:
    random_angle = random.choice(DIRECTIONS)
    turtle1.color(random.choice(color_data))
    turtle1.setheading(random_angle)
    turtle1.fd(30)

    screen.onkey(stop_game, 'End')



screen.exitonclick()