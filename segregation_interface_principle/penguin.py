from bird_interface import BirdInterface
from swimming_interface import SwimmingBirdInterface

class Penguin(BirdInterface, SwimmingBirdInterface):
    
    def eat(self):
        return 'I can eat!'

    def swim(self):
        return 'I can swim!'