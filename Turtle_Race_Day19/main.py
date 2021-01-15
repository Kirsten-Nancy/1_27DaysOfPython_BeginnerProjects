from turtle import Screen, Turtle
import random
# Create the winner to be displayed

turtle_colors = ["maroon4", "pink", "cyan", "red", "yellow", "green", "black"]
screen = Screen()

screen.update()
screen.setup(width=600, height=600)
screen.bgcolor('lavender')
screen.title("Welcome to our esteemed Turtle Race")
winner = Turtle()
winner.hideturtle()
race_active = False

player_bet = screen.textinput(title="Make a bet ladies and gentlemen", prompt="Who are you betting on this fine day")
def create_turtle(my_turtle_name, y_pos, color):
    # print(my_turtle_name)
    my_turtle_name = Turtle(shape="turtle")
    my_turtle_name.penup()
    my_turtle_name.hideturtle()
    my_turtle_name.speed(0)
    my_turtle_name.showturtle()
    my_turtle_name.color(color)
    my_turtle_name.goto(-290, -150 + y_pos)
    return my_turtle_name


turtle_names = ["Dad", "Jeff", "Korir", "Isa", "Sarah", "Mesh", "Audrey", ]

turtle_objects = []
for i in range(7):
    turtle_objects.append(create_turtle(turtle_names[i], i * 50, turtle_colors[i]))

race_active = True

my_index = 0
while race_active:
    for turtle in turtle_objects:
        if turtle.xcor() > 280:
            winner_index = turtle_objects.index(turtle)
            my_index = winner_index
            if turtle_names[winner_index] == player_bet:
                print("You won the magnificent race!")
            else:
                print(f"Sorry you lose, the winner was {turtle_names[winner_index]}")
                # TODO: display the winner o screen
                # ToDO: gif to occupy entire screen
            print(turtle.pencolor())
            race_active = False
        turtle.fd(random.randint(0, 10))
print(my_index)

winner.write(f"The winner is {turtle_names[my_index]}", align='center', font=('Arial',12,'bold'))


screen.exitonclick()