from abc import ABC, abstractmethod

class CarAbstract(ABC):

    @abstractmethod
    def get_brand(self):
        raise NoImplementedError
    
    @abstractmethod
    def avg_car_price(self):
        raise NoImplementedError

    @abstractmethod
    def number_chairs(self):
        raise NoImplementedError