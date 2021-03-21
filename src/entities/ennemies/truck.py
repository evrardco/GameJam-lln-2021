from arcade.sprite import Sprite
from src.entities.ennemies.base_enemy import BaseEnnemy
from os.path import join
from math import pi
class Truck(BaseEnnemy):
    def __init__(self, *args, **kwargs):
        super().__init__(
                            *args, **kwargs,
                            filename=join("assets", "entities", "ennemies", "basic_truck.png"),
                            scale=0.3,
                        )
        self.speed = 150
        self.radians = 3 * pi/2
        self.dmg = 5
        self.reward = 100
    

