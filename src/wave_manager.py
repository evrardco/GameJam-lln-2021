from typing import Dict
from src.level import Level
from src.entities.ennemies.enemy_factory import new_enemy
class WaveManager:
    def __init__(self, game_level: Level, wave_list: Dict) -> None:
        self.wave_list = wave_list
        self.level = game_level
        self.timer = float('inf')
        self.level_done = False
    
    def next_wave(self):
        if not self.wave_list:
            self.level_done = True
            return
        wave_info = self.wave_list.pop(0)
        self.dt = wave_info["dt"]
        self.num = wave_info["num"]
        self.enemies_to_spawn = []
        for d in wave_info["enemies"]:
            for k, v in d.values():
                self.enemies_to_spawn += [k for _ in range(int(v))]
        self.timer = 0
    
    def on_update(self, delta_time: float):

        if self.level_done:
            return

        self.timer -= delta_time
        if self.timer <= 0:
            if not self.level.enemy_list:
                self.next_wave()
                self.timer = self.level.pause_time
            enemy_type = self.enemies_to_spawn.pop(0)
            self.level.enemy_list.append(new_enemy(enemy_type, self.level))
            self.timer = self.dt



