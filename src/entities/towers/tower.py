from os.path import join
from arcade import Sprite
from arcade import load_texture


class Tower(Sprite):
    def __init__(self, enemies, true_texture, *args, **kwargs):
        super().__init__(join("assets", "empty.jpg"), *args, **kwargs)
        self.range = 100
        self.lvl = 0
        self.true_texture = load_texture(true_texture)
        self.fire_rate = 1  # fire per ms
        self.enemies = enemies
        self.id = Tower.id_counter
        self._elapsed_fire = self.fire_rate
        Tower.id_counter += 1

    def on_update(self, delta_time: float):
        if self.lvl > 0 and (targets := self.targets_in_range()) and self._elapsed_fire >= self.fire_rate:
            self.fire(targets)
            self._elapsed_fire = 0
        
        self._elapsed_fire = min(self._elapsed_fire + delta_time, self.fire_rate)
            
        super().on_update(delta_time=delta_time)

    def targets_in_range(self):
        enemies_in_range = []
        for e in self.enemies:
            if abs(e.center_x - self.center_x) + abs(e.center_y - self.center_y) < self.range:
                enemies_in_range.append(e)

        return enemies_in_range


    def fire(self, targets):
        pass
        # print(f"[Tower {self.id}] {len(targets)} enemies in range")

    def lvl_up(self):
        self.lvl += 1
        self.texture = self.true_texture
    

Tower.id_counter = 0
