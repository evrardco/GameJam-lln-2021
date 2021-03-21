from arcade import load_spritesheet
from os.path import join
from src.entities.ennemies.base_enemy import BaseEnemy
textures = load_spritesheet(join("assets", "entities", "ennemies", "bearer.png"), 64, 64, 2, 4)
texture_delay = 0.1

class Bearer(BaseEnemy):
    def __init__(self, game_level, *args, **kwargs):
        super().__init__(game_level, *args, **kwargs)
        self.texture_index = 0
        self.texture = textures[self.texture_index]
        self.texture_time = texture_delay
        self.speed = 80
        self.scale = 0.5
        self.health = 3
        self.reward = 1

    
    def on_update(self, delta_time):
        self.texture_time -= delta_time
        if self.texture_time <= 0:
            self.texture_index = (self.texture_index + 1) % len(textures)
            self.texture = textures[self.texture_index]
            self.texture_time = texture_delay
        return super().on_update(delta_time)
