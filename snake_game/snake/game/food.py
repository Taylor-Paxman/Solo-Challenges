import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here

class Food(Actor): 
    """The responsibility of Food is to keep track of its appearance and position. Food can move around randomly if asked to do so.

    Stereotype: 
        Service Provider

    Attributes:
        _points = This keeps tracks of the points a player has(int)
    """
    __points = 0

    def __init__(self):
        self.set_text("@")
        self.set_position(Point(random.randint(0,60),random.randint(0,20)))
        self.__points = random.randint(1,5)

    def get_points(self):
        return self.__points

    def reset(self):
        """changes the position to a random one within the boundaries of the screen and reassigns the points to a random number between 1 and 5
        
        Args:
            self (Actor): an instance of Actor.
        """
        self.set_position(Point(random.randint(0,60),random.randint(0,20)))
        self.__points = random.randint(1,5)
        


