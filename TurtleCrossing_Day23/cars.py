from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarCollection:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle()
        car.shape('square')
        car.shapesize(stretch_len=2, stretch_wid=None)
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(300, random.randint(-250, 250))
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.bk(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT