from turtle import Turtle, Screen
from colors import color_data
import random

turtle1 = Turtle()
screen = Screen()
screen.setup(width=1000, height=1000)
screen.colormode(255)
screen.title('Spirograph')
turtle1.speed(10)


for i in range(360//5):
    turtle1.circle(100)
    turtle1.color(random.choice(color_data))
    turtle1.setheading(turtle1.heading() + 5)
    print(i)


screen.exitonclick()