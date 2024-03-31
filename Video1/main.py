#!/usr/bin/env python
# pylint: disable=missing-function-docstring,
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring

from random import randint
import pgzrun  # type: ignore # pylint: disable=E0401

# Game Constants.
WIDTH = 800
HEIGHT = 600
TITLE = "Open, Close, Background and Colors"
ICON = "images/python-logo.png"


class Game:
    def __init__(self):
        self.background = "background"

        self.screen_color = (0, 0, 0)

    def draw(self):
        screen.fill(  # pylint: disable=E0602 # noqa: F821 # type: ignore
            self.screen_color
        )
        screen.blit(  # pylint: disable=E0602 # noqa: F821 # type: ignore
            self.background, (0, 0)
        )

    def update(self):
        pass

    def rand_color(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        self.screen_color = (r, g, b)


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
