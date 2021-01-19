from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data_score.txt') as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.color("white")
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Current Score: {self.score} High Score: {self.high_score}", align='center', font=("Arial", 10, "bold"))

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data_score.txt', mode='w') as file2:
                file2.write(str(self.high_score))
        # Else it's not an important value to keep
        self.score = 0
        self.display_score()

    def increment_score(self):
        """Increments the player score by 1 and
        renders the scoreboard with new values"""
        self.score += 1
        self.display_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", align='center', font=("Arial", 12, "bold"))

# TODO: Create constants for the variable values,ease of updating, if that's a word