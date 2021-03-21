from typing import Dict
from src.level import Level
from src.entities.ennemies.enemy_factory import new_enemy
class WaveManager:
    def __init__(self, game_level: Level, wave_info: Dict) -> None:
        self.dt = wave_info["dt"]
        self.num = wave_info["num"]
        self.level = game_level
    
    def spawn_next_wave(self):
        wave = self.waves.pop(0)
