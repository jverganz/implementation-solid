class Car:
    # Constructor of the class
    def __init__(self, brand: str):
        self._brand = brand

    # Return the brand of car
    def get_brand(self):
        return self._brand

