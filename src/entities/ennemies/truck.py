from src.entities.ennemies.base_enemy import BaseEnnemy
from os.path import join
class Truck(BaseEnnemy):
    def __init__(self, path):
        super().__init__(
                            path,
                            filename=join("assets", "sprite.jpg")# "entities", "ennemies", "basic_truck.png")
                        )
    


