from car import Car

class CarDB:
    # Save a car into database
    def save_car(self, car: Car):
        return f'Car {car.get_brand()} save successfully'
        
    # Delete a car of the database
    def delete_car(self, car: Car):
        return f'Car {car.get_brand()} deleted successfully'