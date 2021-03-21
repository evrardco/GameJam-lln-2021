from arcade import Sprite
from numpy.linalg import norm
from src.entities.towers.tower import Tower
from os.path import join

class Projectile(Sprite):
    def __init__(self, target, tower, *args, **kwargs):
        super().__init__(join("assets", "sprite.jpg"), *args, **kwargs, scale=0.5)
        self.dmg = tower.dmg
        self.target = target
        self.projectile_list = tower.projectiles
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
        super().__init__(filename=join("assets", "sprite.jpg"), *args, **kwargs)

        self.cost = 2
        self.projectiles = []
        self.name = "Redneck"
        self.max_lvl = 5

    def draw(self):
        for p in self.projectiles:
            p.draw()
        return super().draw()

    def on_update(self, delta_time: float):
        for p in self.projectiles:
            p.on_update(delta_time)

        return super().on_update(delta_time)

    def fire(self, targets):
        self.projectiles.append(Projectile(targets[len(targets) - 1], self, center_x=self.center_x, center_y = self.center_y))
        return super().fire(targets)

    def lvl_up(self):
        if not super().lvl_up():
            return False
        
        self.cost += self.lvl * 0.5
        self.dmg += self.lvl
        self.fire_rate += self.lvl * 0.5
        self.range += 5
        
        return True
