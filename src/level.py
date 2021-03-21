from src.globals import GAME_WIDTH
from src.entities.towers.tower_spot import TowerSpot
import arcade

import arcade.gui
from arcade.gui import UIManager
import arcade.tilemap
from os.path import join
from src.object_layer import ObjectParser
from src.playerInterface import PlayerInterface
from src.wave_manager import WaveManager

class Level(arcade.View):
    """
    Main view. Really the only view in this example. """
    def __init__(self, id):
        super().__init__()

        self.ui_manager = UIManager()
        self.id = id

        self.mouse_coords = (-1, -1)

    def on_draw(self):
        """ Draw this view. GUI elements are automatically drawn. """
        arcade.start_render()
        self.map.draw()

        for t in self.tower_list:
            t[0].draw()
            if len(t) > 1:
                t[1].draw()

        for e in self.enemy_list:
            e.draw()

    def on_update(self, delta_time: float):
        self.wave_manager.on_update(delta_time)
        for e in self.enemy_list:
            e.on_update(delta_time)

        for t in self.tower_list:
            if len(t) > 1:
                t[1].on_update(delta_time)

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

        tilemap = arcade.tilemap.read_tmx(join("assets", "maps", f"level_{self.id}.tmx"))
        self.map = arcade.tilemap.process_layer(tilemap, 'Calque de Tuiles 1')
        oparser = ObjectParser(self.id)
        
        self.path = oparser.path_finding

        self.enemy_list = []

        self.projectile_list = []

        self.tower_list = []
        for p in oparser.tower_spots:
            self.tower_list.append([TowerSpot(center_x=p["x"], center_y=self.window.height - p["y"])])


        self.max_votes = oparser.max_votes
        self.votes = 0
        self.followers = oparser.followers
        self.pause_time = oparser.pause_time

        self.wave_manager = WaveManager(self, oparser.waves)
        self.interface = PlayerInterface(self)

        self.selected_tower = None


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if x > GAME_WIDTH:
            return

        for t in self.tower_list:
            if t[0].collides_with_point(self.mouse_coords):
                if self.selected_tower:
                    self.set_selected_tower(False)
                self.selected_tower = t
                self.set_selected_tower(True)
                return
            self.set_selected_tower(False)


    def set_selected_tower(self, val):
        if self.selected_tower:
            self.selected_tower[0].selected = val
            if len(self.selected_tower) > 1:
                self.selected_tower[1].selected = val

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.mouse_coords = (x, y)

    def set_votes(self, val):
        self.votes = val
        self.interface.update_votes()

    def set_followers(self, val):
        self.followers = val
        self.interface.update_followers()

    def next_level(self):
        if self.wave_manager.level_done:
            self.window.show_view(Level(self.id + 1))
        else:
            print(f"You must finish this level!")
