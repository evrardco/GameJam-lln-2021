from os.path import join
from arcade.sprite import Sprite
from numpy.linalg import norm


class BaseEnnemy(Sprite):
    def __init__(self, path, enemies, *args, **kwargs):
        super().__init__(join("assets", "sprite.jpg"), *args, **kwargs)
        self.path = path.copy()
        self.curr_node = self.path.pop(0)
        self.speed = 80
        self.center_x, self.center_y = self.curr_node["x"], 800 - self.curr_node["y"]
        self.vel_x, self.vel_y = (0, 0)
        self.health = 10
        self.enemies = enemies

    
    def on_update(self, delta_time):
        if self.health <= 0:
            self.enemies.remove(self)

        nx, ny = self.curr_node["x"], 800 - self.curr_node["y"]

        if norm((self.center_x - nx, self.center_y - ny)) <= (1 + (self.speed/100)*2):
            self.curr_node = self.path.pop(0)
            nx, ny = self.curr_node["x"], 800 - self.curr_node["y"]
            self.vel_x, self.vel_y = nx - self.center_x, ny - self.center_y
            length = norm((self.vel_x, self.vel_y))
            self.vel_x, self.vel_y = self.vel_x / length, self.vel_y / length
        self.center_x += self.vel_x * self.speed * delta_time
        self.center_y += self.vel_y * self.speed * delta_time





