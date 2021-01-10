import turtle as t
import random

my_turtle = t.Turtle()
my_turtle.color("medium spring green")

game_screen = t.Screen()
game_screen.bgcolor("thistle")
t.colormode(255)


# Colors
def random_colors():
    """Generates a tuple of random colors"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# Draw shapes 3-11 sides
def multiple_shape(no_of_sides):
    my_turtle.pencolor(random_colors())
    for _ in range(no_of_sides):
        my_turtle.forward(100)
        my_turtle.right(360 / no_of_sides)


for i in range(3, 11):
    multiple_shape(i)

# Random walk
def random_walk():
    my_turtle.pencolor(random_colors())
    distance = 40
    my_turtle.fd(distance)
    angle = random.choice([0, 90, 180, 270])
    my_turtle.setheading(angle)


for _ in range(100):
    my_turtle.pensize(15)
    random_walk()

# spirograph
my_turtle.speed(10)
def spirograph(n):
    my_turtle.pencolor(random_colors())
    my_turtle.circle(100)
    my_turtle.setheading(n*5)


for i in range(360):
    my_turtle.pensize(5)
    spirograph(i)

game_screen.exitonclick()
