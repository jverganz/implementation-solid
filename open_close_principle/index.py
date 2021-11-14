"""
Open/Close Principle
"""

from car_kia import Kia
from car_nissan import Nissan

def print_avg_car_price(cars):
    for car in cars:
        print(f'{car.get_brand()} avg is: {str(car.avg_car_price())}')

def main():
    # Instances car
    car_kia     = Kia()
    car_nissan  = Nissan()
    cars = [ car_kia, car_nissan ]
    
    print_avg_car_price(cars)

main()