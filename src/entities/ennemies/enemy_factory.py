from src.entities.ennemies.base_enemy import BaseEnemy
from src.entities.ennemies.truck import Truck
def new_enemy(type: str, level) -> BaseEnemy:
    if type == "truck":
        return Truck(level)
