""" We dashin' now. """

import math
import os
from random import randint
#from profilehooks import profile
import pygame
import constants as c
from spritesheet_functions import SpriteSheet

class SpriteHelper:
    """ We need a better way of addressing sprite locations.
        Create a loop to make a 7x8 lookup table. """

    def __init__(self):
        self.matrix = [[(x * 32, y * 32) for x in range(7)] for y in range(8)]

    def lookup(self, coords):
        """ Looks up in which row and column that a certain set of coordinates are.
            Seriously, a lot better than before. """

        x = coords[0]
        y = coords[1]
        return self.matrix[y][x][0], self.matrix[y][x][1]

class Coin(pygame.sprite.Sprite):
    """ Deals with the variables for items that the player must pick up in order to progress.

    Has an x, y, and step for postioning of the coin, and how much the coin should be moved.

    Also, initializes the coin to be a sprite based off of the sprite passed through. """

    def __init__(self, x, y):
        """ In order to make a coin, you need to have a constructor. """

        # Call upon the sprite's constructor.
        super().__init__()

        # Need to have the frame(s) for the coin.
        self.f_coin = []

        # Need to check if things collide (use sprites!)
        self.mask = None

        sprite_sheet = SpriteSheet(os.path.join("assets", "sprites.png"))
        lookup_table = [(0, 1)]
        for value in lookup_table:
            pixel_x, pixel_y = SPRITEHELPER.lookup(value)
            image = sprite_sheet.get_image(pixel_x, pixel_y, \
                c.SPRITEWIDTH, c.SPRITEHEIGHT, c.CHROMA)
            self.f_coin.append(pygame.transform.scale(image, \
                (c.SPRITEWIDTH * c.SCALING, c.SPRITEHEIGHT * c.SCALING)))

        self.image = self.f_coin[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """ Update the current position of the coin on the screen. """

        self.image = self.f_coin[0]
        self.mask = pygame.mask.from_surface(self.image)

class Player(pygame.sprite.Sprite):
    """ Deals with the variables for player information: positioning, and how fast they can move.

    Has an x, y, and speed for initial positioning of the player, and how fast they can move.

    Also, initializes the player to be a sprite based off of the sprite passed through."""

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

        # Need this to check if things collide.
        self.mask = None

        sprite_sheet = SpriteSheet(os.path.join("assets", "sprites.png"))

        lookup_table = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (0, 2)]

        for value in lookup_table:
            pixel_x, pixel_y = SPRITEHELPER.lookup(value)
            image = sprite_sheet.get_image(pixel_x, pixel_y, \
                c.SPRITEWIDTH, c.SPRITEHEIGHT, c.CHROMA)
            self.f_idle_front.append(pygame.transform.scale(image, \
                (c.SPRITEWIDTH * c.SCALING, c.SPRITEHEIGHT * c.SCALING)))

        lookup_table = [(4, 4), (5, 4), (6, 4), (0, 5), (1, 5), (2, 5), (3, 5)]

        for value in lookup_table:
            pixel_x, pixel_y = SPRITEHELPER.lookup(value)
            image = sprite_sheet.get_image(pixel_x, pixel_y, \
                c.SPRITEWIDTH, c.SPRITEHEIGHT, c.CHROMA)
            self.f_idle_back.append(pygame.transform.scale(image, \
                (c.SPRITEWIDTH * c.SCALING, c.SPRITEHEIGHT * c.SCALING)))

        lookup_table = [(1, 1), (1, 2), (1, 1), (1, 3), (2, 1), (2, 2), (2, 1), (2, 3), \
                        (3, 1), (3, 2), (3, 1), (3, 3), (4, 1), (4, 2), (4, 1), (4, 3), \
                        (5, 1), (5, 2), (5, 1), (5, 3), (6, 1), (6, 2), (6, 1), (6, 3), \
                        (0, 2), (0, 3), (0, 2)]

        for value in lookup_table:
            pixel_x, pixel_y = SPRITEHELPER.lookup(value)
            image = sprite_sheet.get_image(pixel_x, pixel_y, \
                c.SPRITEWIDTH, c.SPRITEHEIGHT, c.CHROMA)
            self.f_walking_front.append(pygame.transform.scale(image, \
                (c.SPRITEWIDTH * c.SCALING, c.SPRITEHEIGHT * c.SCALING)))

        lookup_table = [(4, 4), (4, 5), (4, 4), (4, 6), (5, 4), (5, 5), (5, 4), (5, 6), \
                        (6, 4), (6, 5), (6, 4), (6, 6), (0, 5), (0, 6), (0, 5), (0, 7), \
                        (1, 5), (1, 6), (1, 5), (1, 7), (2, 5), (2, 6), (2, 5), (2, 7), \
                        (3, 5), (3, 6), (3, 5), (3, 7)]

        for value in lookup_table:
            pixel_x, pixel_y = SPRITEHELPER.lookup(value)
            image = sprite_sheet.get_image(pixel_x, pixel_y, \
                c.SPRITEWIDTH, c.SPRITEHEIGHT, c.CHROMA)
            self.f_walking_back.append(pygame.transform.scale(image, \
                (c.SPRITEWIDTH * c.SCALING, c.SPRITEHEIGHT * c.SCALING)))

        self.image = self.f_idle_front[0]
        self.frame = 0
        self.count = 0
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """ Updates the current position of the rectangle on screen. """

        if self.rect.x + c.SPRITEWIDTH * c.SCALING + self.change_x < c.WINDOWWIDTH:
            if self.rect.x + self.change_x > 0:
                self.rect.x += self.change_x
        if self.rect.y + c.SPRITEHEIGHT * c.SCALING + self.change_y < c.WINDOWHEIGHT:
            if self.rect.y + self.change_y > 0:
                self.rect.y += self.change_y

        # Deal with drawing the right sprite per direction.
        if self.direction == "IF":
            if self.frame + 1 < len(self.f_idle_front):
                if self.count == 11:
                    self.frame += 1
                    self.count = 0
                else:
                    self.count += 1
            else:
                self.frame = 0
            self.image = self.f_idle_front[self.frame]
        elif self.direction == "IB":
            if self.frame + 1 < len(self.f_idle_back):
                if self.count == 11:
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
        self.mask = pygame.mask.from_surface(self.image)

    def move_rightleft(self, magnitude):
        """ Moves the player right or left by changing the magnitude of change_x.
            magnitude = 0: don't move up/down
            magnitude = 1: change x in the right direction (positive)
            magnitude = -1: change x in the left direction (negative) """

        if self.change_y > 0 and magnitude == 0:
            self.direction = "IF"
        elif self.change_y < 0 and magnitude == 0:
            self.direction = "IB"
        elif magnitude == 1:
            if self.change_y > 0:
                self.direction = "WF"
            elif self.change_y < 0:
                self.direction = "WB"
            else:
                self.direction = "WF"
        elif magnitude == -1:
            if self.change_y == 0:
                self.direction = "WF"
            elif self.change_y < 0:
                self.direction = "WB"
            else:
                self.direction = "WF"
        else:
            self.direction = "IF"
        self.change_x = magnitude * 1.0 * self.speed

    def move_updown(self, magnitude):
        """ Moves the player up or down by changing the magnitude of change_y.
            magnitude = 0: don't move up/down
            magnitude = 1: change y in the down direction (positive)
            magnitude = -1: change y in the up direction (negative) """

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

    def current_location(self):
        """ Gives the player's current location. """
        return self.rect.x, self.rect.y


class Padraicula(pygame.sprite.Sprite):
    """ Deals with the variables for the enemies, including positioning and movement.

    Has an x, y, & speed for initial positioning of the character (off screen), and their movement.

    Also, initializes the enemy to be a sprite based off of the sprite passed through. """

    def __init__(self, xy, speed=1):
        """ Constructing an enemy! """

        # Using the parent (sprite) constructor.

        super().__init__()

        self.change_x = 0
        self.change_y = 0
        self.speed = speed
        self.direction = "WF"

        # We have 3 sets of animations: walking forward, walking back, dabbing front.
        self.f_walking_front = []
        self.f_walking_back = []
        self.f_dab_front = []

        # Need to check if things collide (use sprites!)
        self.mask = None

        sprite_sheet = SpriteSheet(os.path.join("assets", "sprites.png"))

        lookup_table = [(0, 0), (1, 0), (0, 0), (2, 0)]

        for value in lookup_table:
            pixel_x, pixel_y = SPRITEHELPER.lookup(value)
            image = sprite_sheet.get_image(pixel_x, pixel_y, \
                c.SPRITEWIDTH, c.SPRITEHEIGHT, c.CHROMA)
            self.f_walking_front.append(pygame.transform.scale(image, \
                (c.SPRITEWIDTH * c.SCALING, c.SPRITEHEIGHT * c.SCALING)))

        lookup_table = [(3, 0), (4, 0), (3, 0), (5, 0)]

        for value in lookup_table:
            pixel_x, pixel_y = SPRITEHELPER.lookup(value)
            image = sprite_sheet.get_image(pixel_x, pixel_y, \
                c.SPRITEWIDTH, c.SPRITEHEIGHT, c.CHROMA)
            self.f_walking_back.append(pygame.transform.scale(image, \
                (c.SPRITEWIDTH * c.SCALING, c.SPRITEHEIGHT * c.SCALING)))

        lookup_table = [(6, 0)]

        for value in lookup_table:
            pixel_x, pixel_y = SPRITEHELPER.lookup(value)
            image = sprite_sheet.get_image(pixel_x, pixel_y, \
                c.SPRITEWIDTH, c.SPRITEHEIGHT, c.CHROMA)
            self.f_dab_front.append(pygame.transform.scale(image, \
                (c.SPRITEWIDTH * c.SCALING, c.SPRITEHEIGHT * c.SCALING)))

        self.image = self.f_walking_front[0]
        self.frame = 0
        self.count = 0
        self.rect = self.image.get_rect()
        self.rect.x = xy[0]
        self.rect.y = xy[1]
        self.mask = pygame.mask.from_surface(self.image)
        self.currently_dabbing = False

    def update(self):
        """ Updates the current position of the rectangle on screen. """

        if self.rect.x + c.SPRITEWIDTH * c.SCALING + self.change_x < c.WINDOWWIDTH:
            if self.rect.x + self.change_x > 0:
                self.rect.x += self.change_x
        if self.rect.y + c.SPRITEHEIGHT * c.SCALING + self.change_y < c.WINDOWHEIGHT:
            if self.rect.y + self.change_y > 0:
                self.rect.y += self.change_y

        # Deal with drawing the right sprite per direction.

        # Secret dab animation.
        if randint(1, 1000) == 1000 and self.direction == "WF":
            self.currently_dabbing = True
            self.image = self.f_dab_front[0]
            self.dabbing_direction = randint(1, 4)
            if self.dabbing_direction == 1:
                self.image = pygame.transform.flip(self.f_dab_front[0], False, False)
            elif self.dabbing_direction == 2:
                self.image = pygame.transform.flip(self.f_dab_front[0], True, False)
            elif self.dabbing_direction == 3:
                self.image = pygame.transform.flip(self.f_dab_front[0], False, True)
            else:
                self.image = pygame.transform.flip(self.f_dab_front[0], True, True)

        if self.currently_dabbing:
            if self.count == 15:
                self.count = 0
                self.direction = "WF"
                self.currently_dabbing = False
            else:
                self.count += 1
        elif self.direction == "WF":
            if self.frame + 1 < len(self.f_walking_front):
                if self.count == 9:
                    self.frame += 1
                    self.count = 0
                else:
                    self.count += 1
            else:
                self.frame = 0
            self.image = self.f_walking_front[self.frame]
        elif self.direction == "WB":
            if self.frame + 1 < len(self.f_walking_back):
                if self.count == 9:
                    self.frame += 1
                    self.count = 0
                else:
                    self.count += 1
            else:
                self.frame = 0
            self.image = self.f_walking_back[self.frame]
        else:
            self.image = self.f_walking_front[0]
        self.mask = pygame.mask.from_surface(self.image)

    def move_rightleft(self, magnitude):
        """ Moves the Padraicula right or left by changing the magnitude of change_x.
            magnitude = 0: don't move up/down
            magnitude = 1: change x in the right direction (positive)
            magnitude = -1: change x in the left direction (negative) """

        self.change_x = magnitude * 1.0 * self.speed

    def move_updown(self, magnitude):
        """ Moves the Padraicula up or down by changing the magnitude of change_y.
            magnitude = 0: don't move up/down
            magnitude = 1: change y in the down direction (positive)
            magnitude = -1: change y in the up direction (negative) """

        if magnitude == -1:
            self.direction = "WB"
        else:
            self.direction = "WF"
        self.change_y = magnitude * 1.0 * self.speed


class App:
    """ Deals with the game itself. """

    def __init__(self):
        self._intro = True
        self._running = True
        self._display_surf = pygame.display.set_mode((c.WINDOWWIDTH, c.WINDOWHEIGHT), \
            pygame.HWSURFACE)
        self._clock = None
        self.floor = pygame.transform.scale(pygame.image.load(os.path.join("assets", \
            "Floor.png")), (c.WINDOWWIDTH * 2, c.WINDOWHEIGHT * 2)).convert()
        self.player_sprites = pygame.sprite.Group()
        self.pickup_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.player = Player()
        self.coin_count = 0
        self.spawned = False
        self.player_sprites.add(self.player)
        self.pickup_sprites.add(Coin(randint(10, c.WINDOWWIDTH - 10), \
            randint(10, c.WINDOWHEIGHT - 10)) for x in range(3))

    def on_init(self):
        """ On initialization, we have to set a few constants for our game to run.

        This starts up the pygame instance, sets a few constants and its rendering type, and the
        images used for the game itself. This also loads and sets the music. """

        pygame.init()
        pygame.display.set_caption('Pad-Dash')
        self._clock = pygame.time.Clock()
        self._running = True

        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join("assets", "background_music.mp3"))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

    def on_loop(self):
        """ Deals with conditions that need to be checked every iteration of the game. """

        pickups_hit = pygame.sprite.spritecollide(self.player, self.pickup_sprites, \
            False, pygame.sprite.collide_mask)
        if pickups_hit:
            """ Deal with player touching any sprites which are pickups.
                This can be extended to just more than coins. """

            self.coin_count += 1

            """ Instead of having it spawn in a random spot, we'll split it to the four
                quadrants that the game provides, and we try to spawn one in a different
                quadrant. """

            quadrants = [(0, 0), (c.WINDOWWIDTH / 2, 0), \
                (c.WINDOWHEIGHT / 2, 0), (c.WINDOWHEIGHT / 2, c.WINDOWHEIGHT / 2)]

            player_position = self.player.current_location()
            player_quadrant = -1

            if 0 <= player_position[0] < c.WINDOWHEIGHT / 2:
                # Upper half of the board.
                if 0 <= player_position[1] < c.WINDOWWIDTH / 2:
                    # Upper left.
                    player_quadrant = 0
                else:
                    # Upper right.
                    player_quadrant = 1
            else:
                # Lower half of the board.
                if 0 <= player_position[1] < c.WINDOWWIDTH / 2:
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

            x_scaling = (c.SPRITEWIDTH * c.SCALING // 2)
            y_scaling = (c.SPRITEHEIGHT * c.SCALING // 2)
            pickups_hit[0].rect.x = quadrants[coin_quadrant][0] + \
                (randint(1, (c.WINDOWWIDTH // 2) // x_scaling - 1) * x_scaling) + \
                randint(-16, 16)
            pickups_hit[0].rect.y = quadrants[coin_quadrant][1] + \
                randint(1, (c.WINDOWHEIGHT // 2) // y_scaling - 2) * y_scaling + \
                randint(-16, 16)

        if self.coin_count % 2 == 0:
            # Deals with Padraicula spawning.
            if self.coin_count > 0 and not self.spawned:
                # Try to spawn him in the furthest corner.
                spawn_locations = [(10, 10), (1450, 10), (10, 750), (1450, 750)]
                player_location = self.player.current_location()
                furthest_distance = -1
                spawn_at = 0
                for index, spawn in enumerate(spawn_locations):
                    distance = math.sqrt((player_location[0] - spawn[0]) ** 2 + \
                        (player_location[1] - spawn[1]) ** 2)
                    if distance > furthest_distance:
                        furthest_distance = distance
                        spawn_at = index
                enemy = Padraicula(spawn_locations[spawn_at])
                self.enemy_sprites.add(enemy)
                self.spawned = True
        else:
            if self.spawned:
                self.spawned = False

        for pad in self.enemy_sprites:
            if pad.rect.x > self.player.rect.x:
                pad.move_rightleft(-1)
            elif pad.rect.x < self.player.rect.x:
                pad.move_rightleft(1)
            elif pad.rect.x == self.player.rect.x:
                pad.move_rightleft(0)

            if pad.rect.y > self.player.rect.y:
                pad.move_updown(-1)
            elif pad.rect.y < self.player.rect.y:
                pad.move_updown(1)
            elif pad.rect.y == self.player.rect.y:
                pad.move_updown(0)

            if pygame.sprite.spritecollide(self.player, self.enemy_sprites, \
                    False, pygame.sprite.collide_mask):
                self._running = False

    def on_render(self):
        """ Deals with rendering things on screen. """
        self._display_surf.blit(self.floor, (0, 0))
        self.player_sprites.draw(self._display_surf)
        self.pickup_sprites.draw(self._display_surf)
        self.enemy_sprites.draw(self._display_surf)
        score_font = pygame.font.Font(os.path.join("assets", "LCD_solid.ttf"), 64)
        score_surf, score_rect = self.text_objects(str(self.coin_count), \
            score_font, (255, 255, 255))
        score_rect.center = ((c.WINDOWWIDTH / 2), 64)
        self._display_surf.blit(score_surf, score_rect)
        pygame.display.flip()

    def text_objects(self, text, font, input_color):
        """ Takes in text, a font, and the color you want, and produces a text surface. """

        text_surface = font.render(text, True, input_color)
        return text_surface, text_surface.get_rect()

    def button(self, msg, x, y, w, h, ic, ac):
        """ Creates a button which returns true if click is triggered. Otherwise,
            stays where it's placed. """

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self._display_surf, ac, (x, y, w, h))

            if click[0] == 1:
                return True
        else:
            pygame.draw.rect(self._display_surf, ic, (x, y, w, h))

        small_text = pygame.font.Font(os.path.join("assets", "chiller.ttf"), 50)
        text_surf, text_rect = self.text_objects(msg, small_text, c.BLACK)
        text_rect.center = ((x + (w / 2)), (y + (h / 2)))
        self._display_surf.blit(text_surf, text_rect)

    #@profile
    def on_execute(self):
        """ The function which runs the main game loop. Calls other functions
            to check or not to continue looping and rendering what is on screen. """

        if self.on_init() is False:
            self._running = False

        pressed = [0, 0, 0]
        special_keys = [pygame.K_r, pygame.K_i, pygame.K_p]
        while self._intro:
            self._display_surf.fill(c.BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == special_keys[0]:
                        pressed[0] = 1
                    if event.key == special_keys[1]:
                        pressed[1] = 1
                    if event.key == special_keys[2]:
                        pressed[2] = 1
                if event.type == pygame.KEYUP:
                    if event.key == special_keys[0]:
                        pressed[0] = 0
                    if event.key == special_keys[1]:
                        pressed[1] = 0
                    if event.key == special_keys[2]:
                        pressed[2] = 0
            if sum(pressed) == 3:
                rip_text = pygame.font.Font(os.path.join("assets", "chiller.ttf"), 20)
                text_surf, text_rect = self.text_objects("RIP Sean", rip_text, c.DARKRED)
                text_rect.center = ((c.WINDOWWIDTH / 2), (c.WINDOWHEIGHT / 2))
                self._display_surf.blit(text_surf, text_rect)

            large_text = pygame.font.Font(os.path.join("assets", "chiller.ttf"), 115)
            text_surf, text_rect = self.text_objects("Pad-Dash", large_text, c.DARKRED)
            text_rect.center = ((c.WINDOWWIDTH / 2), (c.WINDOWHEIGHT / 3))
            self._display_surf.blit(text_surf, text_rect)

            if self.button("Begin", (c.WINDOWWIDTH/2 - 105), (c.WINDOWHEIGHT/2 + 35), \
                210, 70, c.DARKRED, c.LIGHTRED):
                self._running = True
                self._intro = False

            if self.button("Quit", (c.WINDOWWIDTH/2 - 105), (2* (c.WINDOWHEIGHT/3) + 35), \
                210, 70, c.DARKRED, c.LIGHTRED):
                self._running = False
                self._intro = False

            pygame.display.update()

        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

                right = (pygame.K_RIGHT, pygame.K_d)
                left = (pygame.K_LEFT, pygame.K_a)
                up = (pygame.K_UP, pygame.K_w)
                down = (pygame.K_DOWN, pygame.K_s)

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

            self.player_sprites.update()
            self.pickup_sprites.update()
            self.enemy_sprites.update()
            self.on_loop()
            self.on_render()
            self._clock.tick(60)
            pygame.display.set_caption('Pad-Dash | FPS: {0:.2f}'.format(self._clock.get_fps()))

        pygame.quit()


if __name__ == "__main__":
    SPRITEHELPER = SpriteHelper()
    PADDASH = App()
    PADDASH.on_execute()
