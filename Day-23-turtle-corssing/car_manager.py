import random
from car import Car

START_YCOR = -280
END_YCOR = 280
START_XCOR = 320
MIN_ROW_DIST = 45
MIN_CAR_DIST = 60
MAX_CAR_DIST = 120

cars = {}


def car_maker():
    # For row of cars
    for i in range(START_YCOR, END_YCOR, MIN_ROW_DIST):
        car_row_position = START_XCOR
        cars[i] = []
        # print(f"ycor = {i}")
        # For number of cars in a row
        for j in range(100):
            temp_car = Car()
            cars[i].append(temp_car)
            # temp(car=temp_car, car_row_position=car_row_position, ycor=i)
            # print(f"position is ({car_row_position}, {i})")
            temp_car.goto(car_row_position, i)
            car_distance = random.randint(MIN_CAR_DIST, MAX_CAR_DIST)
            # print(f"car distance is {car_distance}")
            # print(f"old xcor is {car_row_position}")
            car_row_position += car_distance
            # print(f"new xcor is {car_row_position}")
