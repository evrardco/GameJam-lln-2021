from arcade import Sprite
from arcade import draw_rectangle_outline
from arcade import color

class TowerSpot(Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.selected = False
    
    def draw(self):
        if self.selected:
            draw_rectangle_outline(self.center_x, self.center_y, 32, 32, color.RED, 4)
        super().draw()
