import turtle
import random

my_turtle = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)


color_data = [(43, 105, 171), (233, 206, 116), (225, 152, 87), (183, 50, 77), (118, 87, 50), (228, 120, 147),
              (214, 61, 80), (109, 110, 188), (130, 175, 210), (115, 185, 139), (55, 176, 110), (116, 168, 37),
              (202, 18, 42), (33, 56, 113), (221, 61, 50), (26, 142, 108)]



screen.listen()

my_turtle.pencolor(random.choice(color_data))


def forward():
    my_turtle.fd(20)
def backwards():
    my_turtle.bk(20)
def counter_clockwise():
    my_turtle.left(10)
def clockwise():
    my_turtle.right(10)
def clear():
    my_turtle.reset()


screen.onkeypress(forward, 'w')
screen.onkeypress(backwards, 's')
screen.onkeypress(counter_clockwise, 'a')
screen.onkeypress(clockwise, 'd')
screen.onkeypress(clear, 'c')

screen.exitonclick()