from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.color("white")
        # self.write("Welcome to the Snake 3310", font=('Arial', 16, 'bold'), align='center', move=False)
        self.display_score()

    def display_score(self):
        self.write(f"Current Score: {self.score}", align='center', font=("Arial", 10, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align='center', font=("Arial", 12, "bold"))

    def track_score(self):
        self.score += 1
        self.clear()
        self.display_score()

# TODO: Create constants for the variable values,ease of updating, if that's a word