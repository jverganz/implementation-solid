from car_abstract import CarAbstract

class Nissan(CarAbstract):

    def get_brand(self):
        return 'Nissan'

    # Return value average of car Nissan
    def avg_car_price(self):
        return 80000