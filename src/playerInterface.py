import arcade
import arcade.gui
from src.entities.towers.police import Police
from src.globals import GAME_WIDTH
from src.entities.towers.redneck import Redneck
from src.entities.towers.covid import CovidTower


class WaveButton(arcade.gui.UIFlatButton):
    def __init__(self, game_level, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_level = game_level

    def on_click(self):
        self.game_level.next_level()

class TowerButton(arcade.gui.UIFlatButton):
    def __init__(self, game_level, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_level = game_level

    def on_click(self):
        selected_t = self.game_level.selected_tower
        if len(selected_t) < 2:
            new_t = None
            if self.text == "Redneck":
                new_t = Redneck(self.game_level, center_x=selected_t[0].center_x, center_y=selected_t[0].center_y)
            elif self.text == "5G":
                new_t = CovidTower(self.game_level, center_x=selected_t[0].center_x, center_y=selected_t[0].center_y)
            elif self.text == "Police":
                new_t = Police(self.game_level, center_x=selected_t[0].center_x, center_y=selected_t[0].center_y)
            else:
                return
            if self.game_level.followers < new_t.cost:
                return
            new_t.selected = True
            selected_t.append(new_t)
            new_t.lvl_up()
        elif selected_t[1].name == self.text:
            self.game_level.selected_tower[1].lvl_up()


class PlayerInterface():
    def __init__(self, game_level):
        super().__init__()
        self.game_level = game_level
    
        self.game_level.ui_manager.add_ui_element(arcade.gui.UILabel(
            "Followers:",
            center_x=GAME_WIDTH + 100,
            center_y=700,
            width=200,
        ))

        self.ui_followers = arcade.gui.UILabel(
            f"{self.game_level.followers}",
            center_x=GAME_WIDTH + 100,
            center_y=650,
            width=200,
            height=25
        )
        self.game_level.ui_manager.add_ui_element(self.ui_followers)

        self.game_level.ui_manager.add_ui_element(arcade.gui.UILabel(
            "Votes counted:",
            center_x=GAME_WIDTH + 100,
            width=200,
            center_y=600
        ))

        self.ui_votes = arcade.gui.UILabel(
            f"{self.game_level.votes}/{self.game_level.max_votes}",
            center_x=GAME_WIDTH + 100,
            center_y=550,
            width=200,
            height=25
        )
        self.game_level.ui_manager.add_ui_element(self.ui_votes)

        self.game_level.ui_manager.add_ui_element(arcade.gui.UILabel(
            "Buildings:",
            center_x=GAME_WIDTH + 100,
            center_y=300,
            width=200,
            height=25
        ))


        waveButton = WaveButton(
            self.game_level,
            'Next level',
            center_x=GAME_WIDTH + 100,
            center_y=50,
            width=200,
            height=50
        )

        self.game_level.ui_manager.add_ui_element(waveButton)

        towerButton1 = TowerButton(
            self.game_level,
            'Redneck',
            center_x=GAME_WIDTH + 100,
            center_y=250,
            width=200,
            height=50
        )

        self.game_level.ui_manager.add_ui_element(towerButton1)

        towerButton2 = TowerButton(
            self.game_level,
            '5G',
            center_x=GAME_WIDTH + 100,
            center_y=200,
            width=200,
            height=50
        )

        self.game_level.ui_manager.add_ui_element(towerButton2)

        towerButton3 = TowerButton(
            self.game_level,
            'Police',
            center_x=GAME_WIDTH + 100,
            center_y=150,
            width=200,
            height=50
        )

        self.game_level.ui_manager.add_ui_element(towerButton3)

    def update_votes(self):
        self.ui_votes.text = f"{self.game_level.votes}/{self.game_level.max_votes}"

    def update_followers(self):    
        self.ui_followers.text = f"{self.game_level.followers}"
    
