from arcade import Sprite
from numpy.linalg import norm
from src.entities.towers.tower import Tower
from os.path import join

class Projectile(Sprite):
    def __init__(self, target, projectile_list, *args, **kwargs):
        super().__init__(join("assets", "sprite.jpg"), *args, **kwargs, scale=0.5)
        self.dmg = 1
        self.target = target
        self.projectile_list = projectile_list
        self.speed = 250

    def on_update(self, delta_time: float):
        vel_x = (self.center_x - self.target.center_x) * delta_time
        vel_y = (self.center_y - self.target.center_y) * delta_time
        vel_n = norm((vel_x, vel_y))
        vel_x /= vel_n
        vel_y /= vel_n

        self.center_x -= vel_x * delta_time * self.speed
        self.center_y -= vel_y * delta_time * self.speed

        if self.collides_with_sprite(self.target):
            self.target.health -= self.dmg
            self.projectile_list.remove(self)

        return super().on_update(delta_time=delta_time)


class Redneck(Tower):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, true_texture=join("assets", "sprite.jpg"))

        self.projectiles = []

    def draw(self):
        for p in self.projectiles:
            p.draw()

        return super().draw()

    def on_update(self, delta_time: float):
        for p in self.projectiles:
            p.on_update(delta_time)

        return super().on_update(delta_time)

    def fire(self, targets):
        self.projectiles.append(Projectile(targets[0], self.projectiles, center_x=self.center_x, center_y = self.center_y))
        return super().fire(targets)

    def lvl_up(self):
        return super().lvl_up()
