import turtle
import random

turtle.colormode(255)

my_turtle = turtle.Turtle()
screen = turtle.Screen()

color_data = [(43, 105, 171), (233, 206, 116), (225, 152, 87), (183, 50, 77), (118, 87, 50), (228, 120, 147),
              (214, 61, 80), (109, 110, 188), (130, 175, 210), (115, 185, 139), (55, 176, 110), (116, 168, 37),
              (202, 18, 42), (33, 56, 113), (221, 61, 50), (26, 142, 108)]

# Moving the turtle to the bottom
my_turtle.hideturtle()
my_turtle.penup()
my_turtle.goto(-250.0, -250.0)
my_turtle.showturtle()

def hirst_painting():
    for i in range(10):
        my_turtle.dot(20, random.choice(color_data))
        # To prevent it from moving forward at the last iteration
        if i == 9:
            break
        my_turtle.fd(50)

    my_turtle.left(90)
    my_turtle.fd(50)
    my_turtle.setx(-250)


for _ in range(10):
    hirst_painting()
    my_turtle.setheading(0)

screen.exitonclick()