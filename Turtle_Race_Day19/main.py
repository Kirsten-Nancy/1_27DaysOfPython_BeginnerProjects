import random
import time
from turtle import Screen, Turtle

from named_turtle import CustomTurtle

colors = ["Yellow", "Indigo", "Blue", "DeepPink", "RosyBrown", "MediumSpringGreen","red"]

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.title('Turtle Race')
screen.tracer(0)

turtles = [CustomTurtle(name) for name in ("Audrey", "Dad", "Jeff", "Korir", "Isa", "Sarah", "Mesh")]

player_bet = screen.textinput(title="Make a bet ladies and gentlemen", prompt="Enter player name")

for i in range(len(turtles)):
    turtle = turtles[i]
    turtle.shape('turtle')
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(-280, -150 + i * 50)
screen.update()

def draw_lines(initial_pos, angle):
    lines = []
    for j in range(14):
        finishing_line = Turtle('square')
        finishing_line.penup()
        finishing_line.goto(initial_pos)
        finishing_line.color('black')
        finishing_line.setheading(angle)
        finishing_line.color('black')
        finishing_line.fd(j * 40)
        lines.append(finishing_line)


for _ in range(2):
    draw_lines((240, 270), 270)
    draw_lines((260, -270), 90)

race_is_active = True

win_index = 0

while race_is_active:
    for turtle in turtles:
        time.sleep(0.001)
        screen.update()
        if turtle.xcor() > 210:
            turtle.hideturtle()
            turtle.goto(-100, 0)
            if turtle.name == player_bet:
                turtle.write('You win race 🥳 ', align='left', font=("Verdana", 12, "bold"))
            else:
                turtle.write(f'{turtle.name} wins the race', align='left', font=("Verdana", 12, "bold"))
            race_is_active = False
        turtle.forward(random.randint(1, 10))


screen.exitonclick()