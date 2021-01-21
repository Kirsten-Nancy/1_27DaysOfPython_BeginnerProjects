from turtle import Turtle, Screen
import pandas

screen = Screen()

screen.title("US States game")
screen.bgpic("blank_states_img.gif")

# def get_x_y_coordinates(x, y):
#     print(x, y)
#
#
# screen.onclick(get_x_y_coordinates)

count = 0

# Read the data from csv
state_data = pandas.read_csv("50_states.csv")

# Get the states as a list
state_series = state_data["state"]
list_of_states = state_series.to_list()

guessed_states = []

while count < len(list_of_states):
    player_answer = screen.textinput(title=f"{count}/{len(list_of_states)} states correct",
                                     prompt="Guess a state name").title()

    if player_answer == "Exit":
        break
    if player_answer in list_of_states:
        # Get the row
        guessed_states.append(player_answer)
        chosen_state = state_data[state_series == player_answer]
        x_cor = int(chosen_state["x"])
        y_cor = int(chosen_state["y"])
        turtle1 = Turtle()
        turtle1.hideturtle()
        turtle1.penup()
        turtle1.goto(x_cor, y_cor)
        turtle1.write(player_answer)
        count += 1


# Get the difference using XOR op
missed_states = list(set(list_of_states) ^ set(guessed_states))
states_to_study_dict = {
    "state": missed_states
}

states_to_study_dataframe = pandas.DataFrame(states_to_study_dict)
states_to_study_dataframe.to_csv("states_to_study.csv")

# screen.mainloop()