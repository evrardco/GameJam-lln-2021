from src.entities.ennemies.base_enemy import BaseEnnemy
from src.entities.ennemies.truck import Truck
from src.level import Level
def new_enemy(type: str, level: Level) -> BaseEnnemy:
    if type == "truck":
        return Truck(level)
