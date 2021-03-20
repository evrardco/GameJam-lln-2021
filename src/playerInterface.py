import arcade
import arcade.gui
from src.globals import GAME_WIDTH

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


class PlayerInterface():
    def __init__(self, ui_manager):
        super().__init__()
        self.ui_manager = ui_manager
    
        self.ui_manager.add_ui_element(arcade.gui.UILabel(
            "Followers:",
            center_x=GAME_WIDTH + 100,
            center_y=700,
            width=200,
        ))
        
        self.ui_manager.add_ui_element(arcade.gui.UILabel(
            "Votes counted:",
            center_x=GAME_WIDTH + 100,
            width=200,
            center_y=600
        ))

        self.ui_manager.add_ui_element(arcade.gui.UILabel(
            "1000",
            center_x=GAME_WIDTH + 100,
            center_y=650,
            width=200,
            height=25
        ))

        self.ui_manager.add_ui_element(arcade.gui.UILabel(
            "2000",
            center_x=GAME_WIDTH + 100,
            center_y=550,
            width=200,
            height=25
        ))

        self.ui_manager.add_ui_element(arcade.gui.UILabel(
            "Buildings:",
            center_x=GAME_WIDTH + 100,
            center_y=300,
            width=200,
            height=25
        ))


        waveButton = WaveButton(
            'Next Wave',
            center_x=GAME_WIDTH + 100,
            center_y=50,
            width=200,
            height=50
        )

        self.ui_manager.add_ui_element(waveButton)

        towerButton1 = TowerButton(
            'Tower type 1',
            center_x=GAME_WIDTH + 100,
            center_y=250,
            width=200,
            height=50
        )

        self.ui_manager.add_ui_element(towerButton1)

        towerButton2 = TowerButton(
            'Tower type 2',
            center_x=GAME_WIDTH + 100,
            center_y=200,
            width=200,
            height=50
        )

        self.ui_manager.add_ui_element(towerButton2)

        towerButton3 = TowerButton(
            'Tower type 3',
            center_x=GAME_WIDTH + 100,
            center_y=150,
            width=200,
            height=50
        )

        self.ui_manager.add_ui_element(towerButton3)

    
