from turtle import Screen
import time
from cars import CarCollection
from player import Player
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car_collection = CarCollection()
player = Player()
scoreboard = ScoreBoard()

screen.onkey(player.move, 'Up')

game_is_on = True

i = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if i % 6 == 0:
        car_collection.create_car()
    car_collection.move()
    i += 1

    for car in car_collection.cars:
        if car.distance(player) < 20:
            scoreboard.end_game()
            game_is_on = False


    if player.check_finished():
        car_collection.increase_speed()
        scoreboard.increment_score()

screen.exitonclick()