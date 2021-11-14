"""
Segregation Interface Principle
"""

from parrot import Parrot
from penguin import Penguin

def main():

    parrot = Parrot()
    print(f'Parrot: { parrot.eat() } and { parrot.fly() }')

    penguin = Penguin()
    print(f'Penguin: { penguin.eat() } and { penguin.swim() }')

main()