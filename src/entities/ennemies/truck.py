from arcade.sprite import Sprite
from src.entities.ennemies.base_enemy import BaseEnemy
from os.path import join
from math import pi
class Truck(BaseEnemy):
    def __init__(self, *args, **kwargs):
        super().__init__(
                            *args, **kwargs,
                            filename=join("assets", "entities", "ennemies", "basic_truck.png"),
                            scale=0.3,
                        )
        self.max_health = 15
        self.health = self.max_health
        self.speed = 50
        self.radians = 3 * pi/2
        self.dmg = 10
        self.reward = 2
    

