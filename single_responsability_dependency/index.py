"""
Single Responsability Principle
"""

from car import Car
from car_db import CarDB

def main():
    
    # Instance of a car
    car_kia = Car('KIA')
    car_nissan = Car('NISSAN')
    print('Car brand is:', car_kia.get_brand())
    print('Car brand is:', car_nissan.get_brand())

    # Instance of car database
    car_db = CarDB()

    # Save a car
    print(car_db.save_car(car_kia))
    print(car_db.save_car(car_nissan))

    # Delete a car
    print(car_db.delete_car(car_kia))
    print(car_db.delete_car(car_nissan))

main()