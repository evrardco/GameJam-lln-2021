import arcade

import arcade.gui
from arcade.gui import UIManager
from src.level import Level


class MyFlatButton(arcade.gui.UIFlatButton):
    def __init__(self, window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.window = window

    def on_click(self):
        self.window.show_view(Level(self.text))


class Menu(arcade.View):
    def __init__(self):
        super().__init__()

        self.ui_manager = UIManager()

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

        self.ui_manager.add_ui_element(arcade.gui.UILabel(
            self.window.caption,
            center_x=self.window.width // 2,
            center_y=y_slot * 3,
            id="label"
        ))

        button = MyFlatButton(
            self.window,
            'level_1',
            center_x=self.window.width // 2,
            center_y=y_slot * 2,
            width=250,
        )
        self.ui_manager.add_ui_element(button)

