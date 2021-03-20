import arcade
from arcade.gui.ui_style import UIStyle

from src.menu import Menu

if __name__ == "__main__":
    # creates a new class, which will match the id
    UIStyle.default_style().set_class_attrs(
        'label',
        font_color=arcade.color.WHITE,
        font_color_hover=arcade.color.WHITE,
        font_color_press=arcade.color.WHITE,
    )

    window = arcade.Window(title='Democracy defender', height=600, width=800)
    window.show_view(Menu())
    arcade.run()
