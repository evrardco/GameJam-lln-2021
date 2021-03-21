from typing import Dict
from src.entities.ennemies.enemy_factory import new_enemy
class WaveManager:
    def __init__(self, game_level, wave_list: Dict) -> None:
        self.wave_list = wave_list
        self.level = game_level
        self.timer = float('inf')
        self.level_done = False
        self.next_wave()
    
    def next_wave(self):
        if not self.wave_list:
            self.level_done = True
            return
        wave_info = self.wave_list.pop(0)
        self.dt = float(wave_info["dt"])
        self.num = wave_info["num"]
        self.enemies_to_spawn = []
        for d in wave_info["enemies"]:
            for k, v in d.items():
                self.enemies_to_spawn += [k for _ in range(int(v))]
        self.timer = 0
    
    def on_update(self, delta_time: float):
        # print(self.timer)
        if self.level_done:
            return

        self.timer -= delta_time
        if self.timer <= 0:
            if not self.enemies_to_spawn:
                self.next_wave()
                self.timer = self.level.pause_time
                return
            print("Spawning enemy")
            enemy_type = self.enemies_to_spawn.pop(0)
            self.level.enemy_list.append(new_enemy(enemy_type, self.level))
            self.timer = self.dt



