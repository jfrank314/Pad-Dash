#!/usr/bin/env python

""" We dashin' now. """

import inspect
import os
import pygame
from random import randint
from pygame.locals import *

class Coin:
    """
    Deals with the variables for items that the player must pick up in order to progress.

    Has an x, y, and step for postioning of the coin, and how much the coin should be moved.
    """

    x = 0
    y = 0
    step = 44

    def __init__(self, x, y):
        self.x = x * self.step
        self.y = y * self.step

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))


class Player:
    """
    Deals with the variables for player information: positioning, and how fast they can move.

    Has an x, y, and speed for initial positioning of the player, and how fast they can move.
    """

    x = 10
    y = 10
    speed = 8

    def move_right(self):
        """ Moves the player right by adding the speed to the x position. """
        self.x += self.speed

    def move_left(self):
        """ Moves the player left by subtracting the speed to the x position. """
        self.x -= self.speed

    def move_up(self):
        """ Moves the player up by adding the speed to the y position. """
        self.y -= self.speed

    def move_down(self):
        """ Moves the player down by subtracting the speed to the y position. """
        self.y += self.speed


class Padraicula:
    """
    Deals with the variables for the enemies players must avoid, including positioning and movement.

    Has an x, y, & speed for initial positioning of the character (off screen), and their movement.
    """

    x = 801
    y = 601
    speed = 0.5

    def move_right(self):
        """ Moves the player right by adding the speed to the x position. """
        self.x += self.speed

    def move_left(self):
        """ Moves the player left by subtracting the speed to the x position. """
        self.x -= self.speed

    def move_up(self):
        """ Moves the player up by adding the speed to the y position. """
        self.y -= self.speed

    def move_down(self):
        """ Moves the player down by subtracting the speed to the y position. """
        self.y += self.speed


class Game:
    """
    Contains methods that are related to elements within the game state.
    """

    def is_collision(self, object_1, object_2, pad_col=None):
        """ Checks whether or not two objects have collided. """

        if isinstance(object_1, Coin):
            size1 = 26
        else:
            size1 = 52

        if isinstance(object_2, Coin):
            size2 = 26
        else:
            size2 = 52

        x1 = object_1.x
        y1 = object_1.y
        x2 = object_2.x
        y2 = object_2.y
        optional_direction = pad_col

        if optional_direction == "L":
            x1 -= 1
        elif optional_direction == "R":
            x1 += 1
        elif optional_direction == "U":
            y1 -= 1
        elif optional_direction == "D":
            y1 += 1
        else:
            pass

        if x1 >= x2 and x1 <= x2 + size2:
            if y1 >= y2 and y1 <= y2 + size2:
                return True

        if x1 + size1 >= x2 and x1 <= x2 + size2:
            if y1 + size1 >= y2 and y1 <= y2 + size2:
                return True
        return False


class App:
    """
    Deals with the game itself.
    """

    windowWidth = 800
    windowHeight = 600
    player = 0
    coin = 0
    pad = []

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._coin_surf = None
        self._player_surf = None
        self._pad_surf = None
        self._font_score = None
        self._clock = None
        self.game = Game()
        self.player = Player()
        self.coin = Coin(5, 5)
        self.coin_count = 0
        self.spawned = False

    def on_init(self):
        """
        On initialization, we have to set a few constants for our game to run.

        This starts up the pygame instance, sets a few constants and its rendering type, and the
        images used for the game itself. This also loads and sets the music.
        """

        pygame.init()
        pygame.display.set_caption('Pad-Dash')
        self._clock = pygame.time.Clock()
        self._running = True
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        self._player_surf = pygame.image.load(os.path.join("assets", "test_player_img.png")).convert()
        self._coin_surf = pygame.image.load(os.path.join("assets", "test_coin_img.png")).convert()
        self._pad_surf = pygame.image.load(os.path.join("assets", "test_padraicula_img.png")).convert()
        self._font_score = pygame.font.SysFont("monospace", 64)

        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join("assets", "background_music.mp3"))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

    def on_event(self, event):
        """
        Handles the events passed through to the game itself.

        Right now, we're checking if any of the events match QUIT; hitting escape to quit the game.
        """

        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        """
        Deals with conditions that need to be checked every iteration of the game.
        """

        if self.game.is_collision(self.coin, self.player):
            # Deals with coin and player collision.
            self.coin_count += 1
            self.coin.x = randint(2, 9) * 44
            self.coin.y = randint(2, 9) * 44

        if self.coin_count % 2 == 0:
            # Deals with Padraicula spawning.
            if self.coin_count > 0 and not self.spawned:
                self.pad.append(Padraicula())
                self.spawned = True
        else:
            if self.spawned:
                self.spawned = False

        if len(self.pad) == 0:
            pass
        else:
            for pad in self.pad:
                for other_pads in self.pad:
                    if other_pads == pad and len(self.pad) > 1:
                        pass

                    if pad.x > self.player.x and (not self.game.is_collision(pad, other_pads, pad_col="L") or len(self.pad) == 1):
                        pad.move_left()
                    elif pad.x < self.player.x and (not self.game.is_collision(pad, other_pads, pad_col="R") or len(self.pad) == 1):
                        pad.move_right()

                    if pad.y > self.player.y and (not self.game.is_collision(pad, other_pads, pad_col="U") or len(self.pad) == 1):
                        pad.move_up()
                    elif pad.y < self.player.y and (not self.game.is_collision(pad, other_pads, pad_col="D") or len(self.pad) == 1):
                        pad.move_down()

                if self.game.is_collision(pad, self.player):
                    self._running = False

    def on_render(self):
        """
        Deals with rendering things on screen.
        """

        self._display_surf.fill((0, 0, 0))
        self._display_surf.blit(self._player_surf, (self.player.x, self.player.y))
        score_render = self._font_score.render(str(self.coin_count), False, (255, 255, 255))
        self._display_surf.blit(score_render, (700, 10))
        self.coin.draw(self._display_surf, self._coin_surf)

        if not self.pad:
            pass
        else:
            for i in self.pad:
                self._display_surf.blit(self._pad_surf, (i.x, i.y))

        pygame.display.flip()

    def on_cleanup(self):
        """
        Cleans up any unnecessary variables at the end of the game.
        """

        pygame.quit()

    def on_execute(self):
        """
        The function which runs the main game loop. Calls other functions
        to check or not to continue looping and rendering what is on screen.
        """

        if self.on_init() is False:
            self._running = False

        while self._running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if ((keys[K_RIGHT] or keys[K_d]) and self.player.x + 52 < self.windowWidth):
                self.player.move_right()

            if ((keys[K_LEFT] or keys[K_a]) and self.player.x > 0):
                self.player.move_left()

            if ((keys[K_UP] or keys[K_w]) and self.player.y > 0):
                self.player.move_up()

            if ((keys[K_DOWN] or keys[K_s]) and self.player.y + 52 < self.windowHeight):
                self.player.move_down()

            if keys[K_ESCAPE]:
                self._running = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

            self.on_loop()
            self.on_render()
            self._clock.tick(60)
            pygame.display.set_caption('Pad-Dash | FPS: {0:.2f}'.format(self._clock.get_fps()))


        self.on_cleanup()


if __name__ == "__main__":
    THEAPP = App()
    THEAPP.on_execute()
