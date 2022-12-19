from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_new(self):
        random_choice = randint(1, 6)
        if random_choice == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, randint(-250, 250))
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())

    def add_level(self):
        self.car_speed += MOVE_INCREMENT
