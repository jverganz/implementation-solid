from car_abstract import CarAbstract

class Kia(CarAbstract):

    # Return brand of car
    def get_brand(self):
        return 'Kia'

    # Return value average of car Kia
    def avg_car_price(self):
        return 50000

    # Retutn the number chairs of car Kia    
    def number_chairs(self):
        return 5