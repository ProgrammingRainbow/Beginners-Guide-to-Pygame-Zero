#!/usr/bin/env python
# pylint: disable=missing-function-docstring,
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring

import pgzrun  # type: ignore # pylint: disable=E0401

# Game Constants.
WIDTH = 800
HEIGHT = 600
TITLE = "Open and Close"


class Game:
    def draw(self):
        screen.clear()  # pylint: disable=E0602 # noqa: F821 # type: ignore

    def update(self):
        pass


game = Game()


def draw():
    game.draw()


def update():
    game.update()


pgzrun.go()
