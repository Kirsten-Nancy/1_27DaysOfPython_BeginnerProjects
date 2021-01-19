from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.display_score()

    def display_score(self):
        self.goto(-260, 270)
        self.write(f'Level {self.score}')

    def increment_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def end_game(self):
        self.goto(0, 0)
        self.write('Game Over')