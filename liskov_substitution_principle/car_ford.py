from car_abstract import CarAbstract

class Ford(CarAbstract):

    # Return brand of car
    def get_brand(self):
        return 'Ford'

    # Return value average of car Ford
    def avg_car_price(self):
        return 15000

    # Retutn the number chairs of car Ford    
    def number_chairs(self):
        return 8