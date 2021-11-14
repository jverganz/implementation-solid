"""
Liskov Substitution Principle
"""

from car_kia import Kia
from car_nissan import Nissan
from car_ford import Ford

def print_avg_car_price(cars):
    for car in cars:
        print(f'{car.get_brand()} avg is: {car.avg_car_price()} and the chairs is: {car.number_chairs()}')

def main():
    # Instances car
    car_kia     = Kia()
    car_nissan  = Nissan()
    car_ford    = Ford()
    cars = [ car_kia, car_nissan, car_ford ]
    
    print_avg_car_price(cars)

main()