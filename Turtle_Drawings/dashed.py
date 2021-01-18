from turtle import Turtle, Screen

turtle1 = Turtle()
screen = Screen()
screen.setup(width=1000, height=1000)

turtle1.pensize(10)

def move10():
    for _ in range(10):
        turtle1.fd(20)
        print(turtle1.pos())
        turtle1.penup()
        turtle1.fd(20)
        turtle1.pendown()


def draw_square(col):
    turtle1.color(col)
    for _ in range(4):
        move10()
        turtle1.left(90)


turtle1.begin_fill()
draw_square('plum')
turtle1.end_fill()

turtle1.setheading(180)

turtle1.begin_fill()
draw_square('SaddleBrown')
turtle1.end_fill()

screen.exitonclick()