import arcade
from arcade.sprite import Sprite
from numpy.linalg import norm
class BaseEnnemy(Sprite):
    def __init__(self, path, **kwargs):
        super().__init__(**kwargs)
        self.path = path.copy()
        self.curr_node = self.path.pop(0)
        self.speed = 80
        self.center_x, self.center_y = self.curr_node["x"], 800 - self.curr_node["y"]
        self.vel_x, self.vel_y = (0, 0)

    
    def on_update(self, delta_time):

        nx, ny = self.curr_node["x"], 800 - self.curr_node["y"]

        if norm((self.center_x - nx, self.center_y - ny)) <= (1 + (self.speed/100)*2):
            self.curr_node = self.path.pop(0)
            nx, ny = self.curr_node["x"], 800 - self.curr_node["y"]
            self.vel_x, self.vel_y = nx - self.center_x, ny - self.center_y
            length = norm((self.vel_x, self.vel_y))
            self.vel_x, self.vel_y = self.vel_x / length, self.vel_y / length
        self.center_x += self.vel_x * self.speed * delta_time
        self.center_y += self.vel_y * self.speed * delta_time




