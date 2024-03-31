#!/usr/bin/env python
# pylint: disable=missing-function-docstring,
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring

from random import randint
import pgzrun  # type: ignore # pylint: disable=E0401

from pgzero.builtins import (  # type: ignore # pylint: disable=E0401
    Rect,
    Actor,
    keyboard,
    sounds,
    music,
)

# Game Constants.
WIDTH = 800
HEIGHT = 600
TITLE = "Sound Effects and Music"
ICON = "images/python-logo.png"
MUSIC = "freesoftwaresong-8bit"


class Game:
    def __init__(self):
        self.background = "background"

        self.screen_color = (0, 0, 0)

        self.font_size = 80
        self.font_color = (255, 255, 255)
        self.font_name = "freesansbold"
        self.text = "Zero"
        self.text_rect = Rect(
            (0, 0), (self.font_size * len(self.text) / 1.8, self.font_size)
        )
        self.text_vel = 3
        self.text_xvel = self.text_vel
        self.text_yvel = self.text_vel

        self.sprite = Actor("python-logo")
        self.sprite_vel = 5

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
        self.sprite.draw()

    def update(self):
        self.update_text()
        self.update_sprite()

    def rand_color(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        self.screen_color = (r, g, b)
        sounds.python.play()  # type: ignore

    def update_text(self):
        self.text_rect.x += self.text_xvel
        self.text_rect.y += self.text_yvel
        if self.text_rect.left < 0:
            self.text_xvel = self.text_vel
            sounds.zero.play()  # type: ignore
        elif self.text_rect.right > WIDTH:
            self.text_xvel = -self.text_vel
            sounds.zero.play()  # type: ignore
        if self.text_rect.top < 0:
            self.text_yvel = self.text_vel
            sounds.zero.play()  # type: ignore
        elif self.text_rect.bottom > HEIGHT:
            self.text_yvel = -self.text_vel
            sounds.zero.play()  # type: ignore

    def update_sprite(self):
        if keyboard.left or keyboard.a:
            self.sprite.x -= self.sprite_vel
        if keyboard.right or keyboard.d:
            self.sprite.x += self.sprite_vel
        if keyboard.up or keyboard.w:
            self.sprite.y -= self.sprite_vel
        if keyboard.down or keyboard.s:
            self.sprite.y += self.sprite_vel


game = Game()
music.play(MUSIC)


def on_key_down(key):
    if key == key.ESCAPE:
        exit()
    if key == key.SPACE:
        game.rand_color()
    if key == key.M:
        if music.is_playing(MUSIC):
            music.pause()
        else:
            music.unpause()


def draw():
    game.draw()


def update():
    game.update()


pgzrun.go()
