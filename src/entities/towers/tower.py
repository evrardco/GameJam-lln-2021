from arcade import Sprite
from arcade import color
from arcade.draw_commands import draw_circle_outline

class Tower(Sprite):
    def __init__(self, game_level, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.range = 100
        self.max_lvl = 1
        self.lvl = 0
        self.fire_rate = 1  # fire per ms
        self.game_level =game_level
        self.enemies = self.game_level.enemy_list
        self.id = Tower.id_counter
        self.selected = False
        self._elapsed_fire = self.fire_rate
        self.cost = 1
        self.name = "Tower"
        Tower.id_counter += 1

    def draw(self):
        super().draw()
        if self.selected:
            draw_circle_outline(self.center_x, self.center_y, self.range, color.BLUE)

    def on_update(self, delta_time: float):
        targets = self.targets_in_range()
        if self.lvl > 0 and targets and self._elapsed_fire >= self.fire_rate:
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
        # print(f"[Tower {self.id}] {len(targets)} enemies in range")
        pass

    def lvl_up(self):
        if self.game_level.followers < self.cost or self.lvl + 1 > self.max_lvl:
            return
        self.lvl += 1
        self.game_level.set_followers(self.game_level.followers - self.cost)


Tower.id_counter = 0
