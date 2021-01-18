from turtle import Turtle, Screen
from colors import color_data
import random

turtle1 = Turtle()
screen = Screen()
screen.setup(width=600, height=700)
screen.colormode(255)
screen.title('Multiple shapes')



def draw_shape(no_of_sides):
    for _ in range(no_of_sides):
        turtle1.color(random.choice(color_data))
        turtle1.fd(100)
        turtle1.lt(360/no_of_sides)


for i in range(3, 11):
    draw_shape(i)


screen.exitonclick()