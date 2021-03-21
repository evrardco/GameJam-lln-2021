from src.entities.ennemies.truck import Truck
import arcade

import arcade.gui
from arcade.gui import UIManager
import arcade.tilemap
from os.path import join
from src.object_layer import ObjectParser
from src.entities.towers.redneck import Redneck
from src.playerInterface import PlayerInterface
from src.wave_manager import WaveManager

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

        for t in self.tower_list:
            t.draw()

        for e in self.enemy_list:
            e.draw()

    def on_update(self, delta_time: float):
        self.wave_manager.on_update(delta_time)
        for e in self.enemy_list:
            e.on_update(delta_time)

        for t in self.tower_list:
            t.on_update(delta_time)

        if self.votes >= self.max_votes:
            print("GAME OVER")
            exit(0)

        return super().on_update(delta_time)

    def on_show_view(self):
        """ Called once when view is activated. """
        self.setup()
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
    
    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()

        tilemap = arcade.tilemap.read_tmx(join("assets", "maps", f"{self.name}.tmx"))
        self.map = arcade.tilemap.process_layer(tilemap, 'Calque de Tuiles 1')
        oparser = ObjectParser(self.name)
        
        self.path = oparser.path_finding

        self.enemy_list = []
        self.enemy_list.append(Truck(self))

        self.projectile_list = []

        self.tower_list = []
        for p in oparser.tower_spots:
            self.tower_list.append(Redneck(self, center_x=p["x"], center_y=self.window.height - p["y"]))
        
        self.max_votes = oparser.max_votes
        self.votes = 0
        self.followers = oparser.followers
        self.pause_time = oparser.pause_time

        self.wave_manager = WaveManager(self, oparser.waves)
        self.interface = PlayerInterface(self)
        
    
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        for t in self.tower_list:
            if t.collides_with_point(self.mouse_coords):
                t.lvl_up()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.mouse_coords = (x, y)

    def set_votes(self, val):
        self.votes = val
        self.interface.update_votes()

    def set_followers(self, val):
        self.followers = val
        self.interface.update_followers()
