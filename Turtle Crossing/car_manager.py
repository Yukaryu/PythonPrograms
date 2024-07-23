from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
START_MOVE_DIS = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = START_MOVE_DIS

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            new_car.penup()
            new_car.goto(300, rand_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
