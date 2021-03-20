import arcade

import arcade.gui
from arcade.gui import UIManager


class Level(arcade.View):
    """
    Main view. Really the only view in this example. """
    def __init__(self, name):
        super().__init__()

        self.ui_manager = UIManager()
        self.name = name

    def on_draw(self):
        """ Draw this view. GUI elements are automatically drawn. """
        arcade.start_render()

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


