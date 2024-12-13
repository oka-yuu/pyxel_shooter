import pyxel

from lib.config import Config
from lib.player import Player

class App:
    def __init__(self):

        config = Config()

        pyxel.init(config.screen_width, config.screen_height, fps=config.fps, display_scale=3, title=config.title)

        # Player
        self.player = Player(pyxel.width / 2, pyxel.height - 20)

        pyxel.run(self.update, self.draw)

    def update(self):

        self.player.update()

    def draw(self):
        pyxel.cls(0)
        self.player.draw()
App()
