from src.entities.ennemies.base_enemy import BaseEnemy
from src.entities.ennemies.truck import Truck
from src.entities.ennemies.bearer import Bearer
from src.entities.ennemies.reporter import Reporter


def new_enemy(type: str, level) -> BaseEnemy:
    if type == "truck":
        return Truck(level)
    if type == "bearer":
        return Bearer(level)
    if type == "reporter":
        return Reporter(level)