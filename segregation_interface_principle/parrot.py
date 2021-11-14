from bird_interface import BirdInterface
from fly_interface import FlyingBirdInterface

class Parrot(BirdInterface, FlyingBirdInterface):
    def eat(self):
        return 'I can eat!'
    
    def fly(self):
        return 'I can fly!'