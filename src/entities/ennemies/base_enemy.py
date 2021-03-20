from os.path import join
from arcade.sprite import Sprite
from numpy.linalg import norm
from math import pi


class BaseEnnemy(Sprite):
    def __init__(self, path, enemies, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = 300
        self.path = path.copy()
        self.curr_goal = self.path.pop(0)
        self.center_x, self.center_y = self.curr_goal["x"], self.curr_goal["y"]
        self.update_vel(self.curr_goal["turn_dir"])
        self.curr_goal = self.path.pop(0)
        self.health = 10
        self.enemies = enemies

    
    def on_update(self, delta_time):
        if delta_time > 1:
            #delta time post loading is too long
            return
        if self.health <= 0:
            self.enemies.remove(self)
        self.center_x += self.vel_x * self.speed * delta_time
        self.center_y += self.vel_y * self.speed * delta_time

        nx, ny = self.curr_goal["x"], self.curr_goal["y"]
        dist = abs(self.center_x - nx) + abs(self.center_y - ny)
        if dist <= 2 * self.speed * delta_time:
            old_dir = self.dir
            self.center_x, self.center_y = self.curr_goal["x"], self.curr_goal["y"]
            self.update_vel(self.curr_goal["turn_dir"])
            self.rotate(old_dir, self.dir)
            self.curr_goal = self.path.pop(0)


    def update_vel(self, dir):
        x, y = 0, 0
        if dir == "up":
            y = 1
        elif dir == "right":
            x = 1
        elif dir == "down":
            y = -1
        elif dir == "left":
            x = -1
        elif dir == "nil":
            self.vel_x, self.vel_y = x, y
            return
        else:
            raise(Exception(f"Unrecognized direction {dir}"))
        self.vel_x, self.vel_y = x, y
        self.dir = dir

    def rotate(self, old_dir, new_dir):
        if old_dir == "up":
            if new_dir == "right":
                self.radians -= pi/2
            elif new_dir == "down":
                self.radians += 2*pi/2
            elif new_dir == "left":
                self.radians += pi/2
        elif old_dir == "right":
            if new_dir == "up":
                self.radians += pi/2
            elif new_dir == "down":
                self.radians -= pi/2
            elif new_dir == "left":
                self.radians -= 2*pi/2
        elif old_dir == "down":
            if new_dir == "right":
                self.radians -= pi/2
            elif new_dir == "up":
                self.radians -= 2*pi/2
            elif new_dir == "left":
                self.radians -= pi/2
        elif old_dir == "left":
            if new_dir == "right":
                self.radians += 2*pi/2
            elif new_dir == "down":
                self.radians += pi/2
            elif new_dir == "up":
                self.radians -= pi/2



