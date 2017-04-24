#!/usr/bin/env python

""" We dashin' now. """

import os
from random import randint
import pygame
from pygame.locals import *
from spritesheet_functions import SpriteSheet

WIDTH = 32
HEIGHT = 32
SCALING = 4
CHROMA = (0, 255, 0)

class Coin(pygame.sprite.Sprite):
    """
    Deals with the variables for items that the player must pick up in order to progress.

    Has an x, y, and step for postioning of the coin, and how much the coin should be moved.

    Also, initializes the coin to be a sprite based off of the sprite passed through.
    """

    def __init__(self, x, y):
        """ In order to make a coin, you need to have a constructor. """

        # Call upon the sprite's constructor.
        super().__init__()

        # Need to have the frame(s) for the coin.

        self.f_coin = []

        sprite_sheet = SpriteSheet(os.path.join("assets", "sprites.png"))
        image = sprite_sheet.get_image(0, 32, WIDTH, HEIGHT, CHROMA)
        self.f_coin.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))

        self.image = self.f_coin[0]
        self.frame = 0
        self.count = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """ Update the current position of the coin on the screen. """
        self.image = self.f_coin[0]

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
        self.speed = 6
        self.direction = "IF"

        # We have a lot of animations: idle, forward, back idle, back forward.
        self.f_idle_front = []
        self.f_idle_back = []
        self.f_walking_front = []
        self.f_walking_back = []

        sprite_sheet = SpriteSheet(os.path.join("assets", "sprites.png"))

        # First, idle front animation.
        image = sprite_sheet.get_image(32, 32, WIDTH, HEIGHT, CHROMA)
        self.f_idle_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(64, 32, WIDTH, HEIGHT, CHROMA)
        self.f_idle_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(96, 32, WIDTH, HEIGHT, CHROMA)
        self.f_idle_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(128, 32, WIDTH, HEIGHT, CHROMA)
        self.f_idle_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(160, 32, WIDTH, HEIGHT, CHROMA)
        self.f_idle_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(192, 32, WIDTH, HEIGHT, CHROMA)
        self.f_idle_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(0, 64, WIDTH, HEIGHT, CHROMA)
        self.f_idle_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))

        # Next, idle back animation.
        image = sprite_sheet.get_image(128, 128, WIDTH, HEIGHT, CHROMA)
        self.f_idle_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(160, 128, WIDTH, HEIGHT, CHROMA)
        self.f_idle_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(192, 128, WIDTH, HEIGHT, CHROMA)
        self.f_idle_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(0, 160, WIDTH, HEIGHT, CHROMA)
        self.f_idle_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(32, 160, WIDTH, HEIGHT, CHROMA)
        self.f_idle_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(64, 160, WIDTH, HEIGHT, CHROMA)
        self.f_idle_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(96, 160, WIDTH, HEIGHT, CHROMA)
        self.f_idle_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))

        # Next, walking front animation.
        image = sprite_sheet.get_image(32, 64, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(32, 96, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(64, 64, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(64, 96, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(96, 64, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(96, 96, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(128, 64, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(128, 96, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(160, 64, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(160, 96, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(192, 64, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(192, 96, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(0, 96, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(96, 128, WIDTH, HEIGHT, CHROMA)
        self.f_walking_front.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))

        # Next, walking back animation.
        image = sprite_sheet.get_image(128, 160, WIDTH, HEIGHT, CHROMA)
        self.f_walking_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(128, 192, WIDTH, HEIGHT, CHROMA)
        self.f_walking_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(160, 160, WIDTH, HEIGHT, CHROMA)
        self.f_walking_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(160, 192, WIDTH, HEIGHT, CHROMA)
        self.f_walking_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(192, 160, WIDTH, HEIGHT, CHROMA)
        self.f_walking_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(192, 192, WIDTH, HEIGHT, CHROMA)
        self.f_walking_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(0, 192, WIDTH, HEIGHT, CHROMA)
        self.f_walking_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(0, 224, WIDTH, HEIGHT, CHROMA)
        self.f_walking_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(32, 192, WIDTH, HEIGHT, CHROMA)
        self.f_walking_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(32, 224, WIDTH, HEIGHT, CHROMA)
        self.f_walking_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(64, 192, WIDTH, HEIGHT, CHROMA)
        self.f_walking_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(64, 224, WIDTH, HEIGHT, CHROMA)
        self.f_walking_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(96, 192, WIDTH, HEIGHT, CHROMA)
        self.f_walking_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))
        image = sprite_sheet.get_image(96, 224, WIDTH, HEIGHT, CHROMA)
        self.f_walking_back.append(pygame.transform.scale(image, (WIDTH * SCALING, HEIGHT * SCALING)))

        self.image = self.f_idle_front[0]
        self.frame = 0
        self.count = 0
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10

    def update(self):
        """ Updates the current position of the rectangle on screen. """
        if self.rect.x + WIDTH * SCALING + self.change_x < THEAPP.windowWidth:
            if self.rect.x + self.change_x > 0:
                self.rect.x += self.change_x
        if self.rect.y + HEIGHT * SCALING + self.change_y < THEAPP.windowHeight:
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
        elif self.direction == "WB":
            if self.frame + 1 < len(self.f_walking_back):
                if self.count >= 3:
                    self.frame += 1
                    self.count = 0
                else:
                    self.count += 1
            else:
                self.frame = 0
            self.image = self.f_walking_back[self.frame]
        else:
            self.image = self.f_idle_front[0]

    def move_rightleft(self, magnitude):
        """ Moves the player right or left by changing the magnitude of change_x.
            magnitude = 0: don't move up/down
            magnitude = 1: change x in the right direction (positive)
            magnitude = -1: change x in the left direction (negative)
        """
        if self.change_x > 0 and magnitude == 0:
            # we were moving right before, now we're not. we need to show idle front.
            self.direction = "IF"
        elif self.change_x < 0 and magnitude == 0:
            # we were moving left before, now we're not. we need to show idle front.
            self.direction = "IF"
        elif magnitude == 1:
            self.direction = "WF"
        elif magnitude == -1:
            self.direction = "WF"
        else:
            self.direction = "IF"
        self.change_x = magnitude * 1.0 * self.speed

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
        elif magnitude == -1:
            self.direction = "WB"
        else:
            self.direction = "IF"
        self.change_y = magnitude * 1.0 * self.speed


class Padraicula:
    """
    Deals with the variables for the enemies players must avoid, including positioning and movement.

    Has an x, y, & speed for initial positioning of the character (off screen), and their movement.
    """

    x = 801
    y = 601
    speed = 1

    def move_right(self):
        """ Moves the Padraicula right by adding the speed to the x position. """
        self.x += self.speed

    def move_left(self):
        """ Moves the Padraicula left by subtracting the speed to the x position. """
        self.x -= self.speed

    def move_up(self):
        """ Moves the Padraicula up by adding the speed to the y position. """
        self.y -= self.speed

    def move_down(self):
        """ Moves the Padraicula down by subtracting the speed to the y position. """
        self.y += self.speed


class Game:
    """
    Contains methods that are related to elements within the game state.
    """

    def is_collision(self, object_1, object_2, pad_col=None):
        """ Checks whether or not two objects have collided. """

        if isinstance(object_1, Padraicula):
            size1 = 52
        else:
            size1 = WIDTH * 4

        if isinstance(object_2, Padraicula):
            size2 = 52
        else:
            size2 = WIDTH * 4

        x1 = object_1.x if isinstance(object_1, Padraicula) else object_1.rect.x
        y1 = object_1.y if isinstance(object_1, Padraicula) else object_1.rect.y
        x2 = object_2.x if isinstance(object_2, Padraicula) else object_2.rect.x
        y2 = object_2.y if isinstance(object_2, Padraicula) else object_2.rect.y

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
    pad = []

    def __init__(self):
        self._running = True
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        self._pad_surf = None
        self._font_score = None
        self._clock = None
        self.active_sprites = pygame.sprite.Group()
        self.game = Game()
        self.player = Player()
        self.coin = Coin(randint(10, 300), randint(10, 300))
        self.coin_count = 0
        self.spawned = False
        self.active_sprites.add(self.player)
        self.active_sprites.add(self.coin)


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

            """ Instead of having it spawn in a random spot, we'll split it to the four
                quadrants that the game provides, and we try to spawn one in a different
                quadrant.
            """
            quadrants = [(0, 0), (self.windowWidth / 2, 0), \
                (self.windowHeight / 2, 0), (self.windowHeight / 2, self.windowHeight / 2)]

            player_position = (self.player.rect.x, self.player.rect.y)
            player_quadrant = -1

            if 0 <= player_position[0] < self.windowHeight / 2:
                # Upper half of the board.
                if 0 <= player_position[1] < self.windowWidth / 2:
                    # Upper left.
                    player_quadrant = 0
                else:
                    # Upper right.
                    player_quadrant = 1
            else:
                # Lower half of the board.
                if 0 <= player_position[1] < self.windowWidth / 2:
                    # Lower left.
                    player_quadrant = 2
                else:
                    # Lower right.
                    player_quadrant = 3

            coin_quadrant = player_quadrant
            while coin_quadrant == player_quadrant:
                coin_quadrant = randint(0, 3)

            if randint(0, 2) == 2:
                coin_quadrant = player_quadrant

            self.coin.rect.x = quadrants[coin_quadrant][0] + randint(1, 6) * 64
            self.coin.rect.y = quadrants[coin_quadrant][1] + randint(1, 6) * 64

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
                        self.player.move_rightleft(1)
                    if event.key in left:
                        self.player.move_rightleft(-1)
                    if event.key in up:
                        self.player.move_updown(-1)
                    if event.key in down:
                        self.player.move_updown(1)

                if event.type == pygame.KEYUP:
                    if event.key in left or event.key in right:
                        self.player.move_rightleft(0)
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
