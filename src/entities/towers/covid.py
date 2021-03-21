from src.entities.towers.tower import Tower
from os.path import join
from arcade import load_spritesheet

textures = load_spritesheet(join("assets", "entities", "towers", "5G_tower.png"), 64, 64, 2, 4)
texture_delay = 0.1

class CovidTower(Tower):
    def __init__(self, *args, **kwargs):
        super().__init__(filename=join("assets", "sprite.jpg"), *args, **kwargs)

        self.cost = 4
        self.fire_rate = 1.5
        self.dmg = 1

        self.name = "5G"
        self.max_lvl = 5

        self.texture_index = 0
        self.texture = textures[self.texture_index]
        self.texture_time = texture_delay

    def on_update(self, delta_time: float):
        self.texture_time -= delta_time
        if self.texture_time <= 0:
            self.texture_index = (self.texture_index + 1) % len(textures)
            self.texture = textures[self.texture_index]
            self.texture_time = texture_delay

        return super().on_update(delta_time)

    def fire(self, targets):
        for t in targets:
            t.health -= self.dmg
        return super().fire(targets)
    
    def lvl_up(self):
        if not super().lvl_up():
            return False
        
        self.cost += self.lvl * 0.5
        self.dmg += self.lvl
        self.fire_rate += self.lvl * 0.5
        self.range += 5

        return True
