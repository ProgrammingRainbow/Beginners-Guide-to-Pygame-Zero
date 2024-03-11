#!/usr/bin/env python
# pylint: disable=missing-function-docstring,
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring

import random
import pgzrun  # type: ignore # pylint: disable=E0401
from pgzero.builtins import (  # type: ignore # pylint: disable=E0401
    Rect,
)

# Game Constants.
WIDTH = 800
HEIGHT = 600
TITLE = "Moving Text"
ICON = "images/python-logo.png"


class Game:
    def __init__(self):
        self.background = "background"

        self.screen_color = (0, 0, 0)

        self.font_size = 80
        self.font_color = (255, 255, 255)
        self.font_name = "freesansbold.ttf"

        self.text = "Zero"
        self.text_vel = 2
        self.text_xvel = 2
        self.text_yvel = 2
        self.text_rect = Rect(
            (0, 0), (self.font_size * len(self.text) / 1.5, self.font_size)
        )

    def draw(self):
        screen.fill(  # pylint: disable=E0602 # noqa: F821 # type: ignore
            self.screen_color
        )
        screen.blit(  # pylint: disable=E0602 # noqa: F821 # type: ignore
            self.background, (0, 0)
        )
        screen.draw.text(  # pylint: disable=E0602 # noqa: F821 # type: ignore
            self.text,
            self.text_rect.topleft,
            color=self.font_color,
            fontname=self.font_name,
            fontsize=self.font_size,
        )

    def update(self):
        self.update_text()

    def rand_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.screen_color = (r, g, b)

    def update_text(self):
        self.text_rect.x += self.text_xvel
        self.text_rect.y += self.text_yvel
        if self.text_rect.right > WIDTH:
            self.text_xvel = -self.text_vel
        if self.text_rect.left < 0:
            self.text_xvel = self.text_vel
        if self.text_rect.bottom > HEIGHT:
            self.text_yvel = -self.text_vel
        if self.text_rect.top < 0:
            self.text_yvel = self.text_vel


game = Game()


def on_key_down(key):
    if key == key.ESCAPE:
        exit()
    if key == key.SPACE:
        game.rand_color()


def draw():
    game.draw()


def update():
    game.update()


pgzrun.go()
