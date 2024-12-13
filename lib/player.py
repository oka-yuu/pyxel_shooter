import pyxel

from lib.config import Config

class Player:
    def __init__(self, x, y):

        config = Config()

        self.x = x
        self.y = y
        self.w = config.player_width
        self.h = config.player_height
        self.speed = config.player_speed
        self.is_alive = True

        pyxel.images[0].set(
            0,
            0,
            [
                "00c00c00",
                "0c7007c0",
                "0c7007c0",
                "c703b07c",
                "77033077",
                "785cc587",
                "85c77c58",
                "0c0880c0",
            ],
        )

    def update(self):
        if self.push_left():
            self.x -= self.speed

        elif self.push_right():
            self.x += self.speed

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.w, self.h, 0)

    # いずれkeyManagerに
    def push_left(self):
        return pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT)

    def push_right(self):
        return pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT)

