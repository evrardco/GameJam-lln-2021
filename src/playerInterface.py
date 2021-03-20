import arcade
import arcade.gui
from arcade.gui import UIManager



class WaveButton(arcade.gui.UIFlatButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_click(self):
        print("Next Wave is starting !")

class TowerButton(arcade.gui.UIFlatButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_click(self):
        print("Tower type selected !")


class PlayerInterface(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()

    def on_draw(self):
        """ Draw this view. GUI elements are automatically drawn. """
        arcade.start_render()

    def on_show_view(self):
        """ Called once when view is activated. """
        self.setup()
        arcade.set_background_color(arcade.color.BLUE_GREEN)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    
    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()

        self.ui_manager.add_ui_element(arcade.gui.UILabel(
            "Tweeter followers :",
            center_x=600,
            center_y=700
        ))
        
        self.ui_manager.add_ui_element(arcade.gui.UILabel(
            "Votes counted :",
            center_x=600,
            center_y=600
        ))

        self.ui_manager.add_ui_element(arcade.gui.UILabel(
            "1000",
            center_x=600,
            center_y=650,
            width=200,
            height=25
        ))

        self.ui_manager.add_ui_element(arcade.gui.UILabel(
            "2000",
            center_x=600,
            center_y=550,
            width=200,
            height=25
        ))

        waveButton = WaveButton(
            'Next Wave',
            center_x=600,
            center_y=200,
            width=200,
            height=50
        )

        self.ui_manager.add_ui_element(waveButton)

        towerButton1 = TowerButton(
            'Tower type 1',
            center_x=150,
            center_y=700,
            width=200,
            height=50
        )

        self.ui_manager.add_ui_element(towerButton1)

        towerButton2 = TowerButton(
            'Tower type 2',
            center_x=150,
            center_y=400,
            width=200,
            height=50
        )

        self.ui_manager.add_ui_element(towerButton1)

        towerButton3 = TowerButton(
            'Tower type 3',
            center_x=150,
            center_y=200,
            width=200,
            height=50
        )

        self.ui_manager.add_ui_element(towerButton1)

    