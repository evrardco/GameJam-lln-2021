from arcade.sprite import Sprite
from src.helpers import total_rotational_increment


class BaseEnemy(Sprite):
    def __init__(self, game_level, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = 300
        self.path = game_level.path.copy()
        self.curr_goal = self.path.pop(0)
        self.center_x, self.center_y = self.curr_goal["x"], self.curr_goal["y"]
        self.update_vel(self.curr_goal["turn_dir"])
        self.curr_goal = self.path.pop(0)
        self.health = 10
        self.game_level = game_level
        self.enemies = game_level.enemy_list
        self.dmg = 1
        self.reward = 1

    
    def on_update(self, delta_time):
        if delta_time > 1:
            #delta time post loading is too long
            return

        if self.health <= 0:
            self.game_level.set_followers(self.game_level.followers + self.reward)
            self.enemies.remove(self)

        self.center_x += self.vel_x * self.speed * delta_time
        self.center_y += self.vel_y * self.speed * delta_time

        nx, ny = self.curr_goal["x"], self.curr_goal["y"]
        dist = abs(self.center_x - nx) + abs(self.center_y - ny)
        if dist <= 2 * self.speed * delta_time:
            if not self.path:
                self.enemies.remove(self)
                self.game_level.set_votes(self.game_level.votes + self.dmg)
                return
            
            old_dir = self.dir
            
            self.center_x, self.center_y = self.curr_goal["x"], self.curr_goal["y"]
            self.update_vel(self.curr_goal["turn_dir"])
            self.radians += total_rotational_increment(old_dir, self.dir)
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
