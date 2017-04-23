#!/usr/bin/env python

""" We dashin' now. """

import os
from random import randint
import pygame
from pygame.locals import *
from spritesheet_functions import SpriteSheet

WIDTH = 32
HEIGHT = 32
CHROMA = (0, 255, 0)

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
        """ Takes in an image to draw on the surface at a specified position. """
        surface.blit(image, (self.x, self.y))


class Player(pygame.sprite.Sprite):
    """
    Deals with the variables for player information: positioning, and how fast they can move.

    Has an x, y, and speed for initial positioning of the player, and how fast they can move.

    Also, initializes the player to be a sprite based off of the sprite passed through.
    """

    def __init__(self):
        """ Constructing the player... """

        # Let's use the parent (sprite) constructor.
        super().__init__()

        # Need to set initial position and speed of the player.
        self.change_x = 0
        self.change_y = 0
        self.speed = 8
        self.direction = "IF"

        """ We have a lot of animations: idle, forward, left, right (flip left),
            back idle, back forward, back left, back right (flip back left).
        """
        self.f_idle_front = []
        self.f_idle_back = []
        self.f_walking_front = []
        self.f_walking_front_left = []
        self.f_walking_front_right = []
        self.f_walking_back = []
        self.f_walking_back_left = []
        self.f_walking_back_right = []

        sprite_sheet = SpriteSheet(os.path.join("assets", "sprites.png"))

        # First, idle front animation.
        image = sprite_sheet.get_image(32, 32, WIDTH, HEIGHT, CHROMA)
        self.f_idle_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(64, 32, WIDTH, HEIGHT, CHROMA)
        self.f_idle_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(96, 32, WIDTH, HEIGHT, CHROMA)
        self.f_idle_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(128, 32, WIDTH, HEIGHT, CHROMA)
        self.f_idle_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(160, 32, WIDTH, HEIGHT, CHROMA)
        self.f_idle_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(192, 32, WIDTH, HEIGHT, CHROMA)
        self.f_idle_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(0, 64, WIDTH, HEIGHT, CHROMA)
        self.f_idle_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))

        # Next, idle back animation.
        image = sprite_sheet.get_image(128, 128, WIDTH, HEIGHT, CHROMA)
        self.f_idle_back.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(160, 128, WIDTH, HEIGHT, CHROMA)
        self.f_idle_back.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(192, 128, WIDTH, HEIGHT, CHROMA)
        self.f_idle_back.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(0, 160, WIDTH, HEIGHT, CHROMA)
        self.f_idle_back.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(32, 160, WIDTH, HEIGHT, CHROMA)
        self.f_idle_back.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(64, 160, WIDTH, HEIGHT, CHROMA)
        self.f_idle_back.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(96, 160, WIDTH, HEIGHT, CHROMA)
        self.f_idle_back.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))

        # Next, walking front animation.
        image = sprite_sheet.get_image(32, 64, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(32, 96, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(64, 64, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(64, 96, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(96, 64, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(96, 96, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(128, 64, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(128, 96, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(160, 64, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(160, 96, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(192, 64, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(192, 96, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(0, 96, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))
        image = sprite_sheet.get_image(96, 128, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale2x(pygame.transform.scale2x(image)))

        self.image = self.f_idle_front[0]
        self.frame = 0
        self.count = 0
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10

    def update(self):
        """ Updates the current position of the rectangle on screen. """
        if self.rect.x + WIDTH * 2 + self.change_x < THEAPP.windowWidth:
            if self.rect.x + self.change_x > 0:
                self.rect.x += self.change_x
        if self.rect.y + HEIGHT * 2 + self.change_y < THEAPP.windowHeight:
            if self.rect.y + self.change_y > 0:
                self.rect.y += self.change_y

        # Deal with drawing the right sprite per direction.
        if self.direction == "IF":
            if self.frame + 1 < len(self.f_idle_front):
                if self.count == 6:
                    self.frame += 1
                    self.count = 0
                else:
                    self.count += 1
            else:
                self.frame = 0
            self.image = self.f_idle_front[self.frame]
        elif self.direction == "IB":
            if self.frame + 1 < len(self.f_idle_back):
                if self.count == 6:
                    self.frame += 1
                    self.count = 0
                else:
                    self.count += 1
            else:
                self.frame = 0
            self.image = self.f_idle_back[self.frame]
        elif self.direction == "WF":
            if self.frame + 1 < len(self.f_walking_front):
                if self.count >= 3:
                    self.frame += 1
                    self.count = 0
                else:
                    self.count += 1
            else:
                self.frame = 0
            self.image = self.f_walking_front[self.frame]

        else:
            self.image = self.f_idle_front[0]

    def move_right(self):
        """ Moves the player right by adding the speed to the x position. """
        self.change_x = self.speed

    def move_left(self):
        """ Moves the player left by subtracting the speed to the x position. """
        self.change_x = -1. * self.speed

    def move_updown(self, magnitude):
        """ Moves the player up or down by changing the magnitude of change_y. 
            magnitude = 0: don't move up/down
            magnitude = 1: change y in the down direction (positive)
            magnitude = -1: change y in the up direction (negative)
        """
        if self.change_y > 0 and magnitude == 0:
            # we were moving down before, now we're not. we need to show idle front.
            self.direction = "IF"
        elif self.change_y < 0 and magnitude == 0:
            # we were moving up before, now we're not. we need to show idle back.
            self.direction = "IB"
        elif magnitude == 1:
            self.direction = "WF"
        else:
            self.direction = "IF"
        self.change_y = magnitude * 1.0 * self.speed

    def no_move(self, direction):
        """ Player stops moving.
            direction == 0: x direction (left, right)
            direction == 1: y direction (up, down)
            """
        if direction == 0:
            self.change_x = 0
        else:
            self.change_y = 0


class Padraicula:
    """
    Deals with the variables for the enemies players must avoid, including positioning and movement.

    Has an x, y, & speed for initial positioning of the character (off screen), and their movement.
    """

    x = 801
    y = 601
    speed = 1

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

        x1 = object_1.x if not isinstance(object_1, Player) else object_1.rect.x
        y1 = object_1.y if not isinstance(object_1, Player) else object_1.rect.y
        x2 = object_2.x if not isinstance(object_2, Player) else object_2.rect.x
        y2 = object_2.y if not isinstance(object_2, Player) else object_2.rect.y

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

    windowWidth = 1600
    windowHeight = 900
    player = 0
    coin = 0
    pad = []

    def __init__(self):
        self._running = True
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        self._coin_surf = None
        self._pad_surf = None
        self._font_score = None
        self._clock = None
        self.active_sprites = pygame.sprite.Group()
        self.game = Game()
        self.player = Player()
        self.coin = Coin(5, 5)
        self.coin_count = 0
        self.spawned = False
        self.active_sprites.add(self.player)

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

        if not self.pad:
            pass
        else:
            for pad in self.pad:
                for other_pads in self.pad:
                    if other_pads == pad and len(self.pad) > 1:
                        pass

                    if pad.x > self.player.rect.x and (not self.game.is_collision(pad, other_pads, pad_col="L") or len(self.pad) == 1):
                        pad.move_left()
                    elif pad.x < self.player.rect.x and (not self.game.is_collision(pad, other_pads, pad_col="R") or len(self.pad) == 1):
                        pad.move_right()

                    if pad.y > self.player.rect.y and (not self.game.is_collision(pad, other_pads, pad_col="U") or len(self.pad) == 1):
                        pad.move_up()
                    elif pad.y < self.player.rect.y and (not self.game.is_collision(pad, other_pads, pad_col="D") or len(self.pad) == 1):
                        pad.move_down()

                if self.game.is_collision(pad, self.player):
                    self._running = False

    def on_render(self):
        """
        Deals with rendering things on screen.
        """

        self._display_surf.fill((128, 128, 128))
        self.active_sprites.draw(self._display_surf)
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
            # pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

                right = (pygame.K_RIGHT, pygame.K_d)
                left = (pygame.K_LEFT, pygame.K_a)
                up = (pygame.K_UP, pygame.K_w)
                down = (pygame.K_DOWN, pygame.K_d)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self._running = False
                    if event.key in right:
                        self.player.move_right()
                    if event.key in left:
                        self.player.move_left()
                    if event.key in up:
                        self.player.move_updown(-1)
                    if event.key in down:
                        self.player.move_updown(1)

                if event.type == pygame.KEYUP:
                    if event.key in left or event.key in right:
                        self.player.no_move(0)
                    if event.key in up or event.key in down:
                        self.player.move_updown(0)

            self.active_sprites.update()
            self.on_loop()
            self.on_render()
            self._clock.tick(60)
            pygame.display.set_caption('Pad-Dash | FPS: {0:.2f}'.format(self._clock.get_fps()))
            pygame.display.flip()

        self.on_cleanup()


if __name__ == "__main__":
    THEAPP = App()
    THEAPP.on_execute()
