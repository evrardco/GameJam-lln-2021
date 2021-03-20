from os import path
import arcade

import arcade.gui
from arcade.gui import UIManager
from arcade.sprite import Sprite
from arcade.sprite_list import SpriteList
import arcade.tilemap
from os.path import join
from src.object_layer import ObjectParser

class Level(arcade.View):
    """
    Main view. Really the only view in this example. """
    def __init__(self, name):
        super().__init__()

        self.ui_manager = UIManager()
        self.name = name

        self.mouse_coords = (-1, -1)

    def on_draw(self):
        """ Draw this view. GUI elements are automatically drawn. """
        arcade.start_render()

        self.map.draw()
        self.path_list.draw()

    def on_show_view(self):
        """ Called once when view is activated. """
        self.setup()
        arcade.set_background_color(arcade.color.BLACK)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()

        y_slot = self.window.height // 4

        # left side elements
        self.ui_manager.add_ui_element(arcade.gui.UILabel(
            self.name,
            center_x=self.window.width // 2,
            center_y=y_slot * 3,
            id="label"
        ))

        tilemap = arcade.tilemap.read_tmx(join("assets", "maps", f"{self.name}.tmx"))
        self.map = arcade.tilemap.process_layer(tilemap, 'Calque de Tuiles 1')
        oparser = ObjectParser(self.name)
        self.path = oparser.path_finding
        self.tower_spots = oparser.tower_spots
        
        self.path_list = SpriteList()
        for p in self.tower_spots:
            self.path_list.append(Sprite(join("assets", "sprite.jpg"), center_x=p["x"], center_y=self.window.height - p["y"], scale=1.0))
        
    
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        for t in self.path_list:
            if t.collides_with_point(self.mouse_coords):
                print("ok")

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.mouse_coords = (x, y)

        


