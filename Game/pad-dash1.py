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

    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step

    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y))

class Player:
    """
    Deals with the variables for player information: positioning, and how fast they can move.

    Has an x, y, and speed for initial positioning of the player, and how fast they can move.
    """

    x = 10
    y = 10
    speed = .2

    def moveRight(self):    #these define the movement of the player
        self.x  += self.speed

    def moveLeft(self):
        self.x -= self.speed

    def moveUp(self):
        self.y -= self.speed

    def moveDown(self):
        self.y += self.speed

class Padraicula:
    """
    Deals with the variables for the enemies players must avoid, including positioning and movement.

    Has an x, y, & speed for initial positioning of the character (off screen), and their movement.
    """

    x = 801
    y = 601
    speed = .025


    def moveRight(self):    #these define the movement of the enemy
        self.x  += self.speed

    def moveLeft(self):
        self.x -= self.speed

    def moveUp(self):
        self.y -= self.speed

    def moveDown(self):
        self.y += self.speed


class Game:
    """
    Contains methods that are related to elements within the game state.
    """

    def isCollision(self, x1, y1, x2, y2, size1, size2):
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
        self.running = True
        self._display_surf = None
        self._coin_surf = None
        self.player = Player()
        self.game = Game()
        self.coin = Coin(5,5)
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
        self._running = True
        self._image_surf = pygame.image.load("test_player_img.png").convert()
        self._coin_surf = pygame.image.load("test_coin_img.png").convert()
        self._pad_surf = pygame.image.load("test_padraicula_img.png").convert()

        pygame.mixer.init()
        pygame.mixer.music.load("background_music.mp3")
        pygame.mixer.music.play(-1)
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

        if self.game.isCollision(self.coin.x, self.coin.y, self.player.x, self.player.y, 26, 52):
            """ Checks whether or not a coin and a player has collided. """
            self.coin_count += 1
            self.coin.x = randint(2, 9) * 44
            self.coin.y = randint(2, 9) * 44

        if self.coin_count % 2 == 0 and self.coin_count > 0 and self.spawned == False:
            """ Checks whether or not to spawn another Padraicula into the game. """
            self.pad.append(Padraicula())
            self.spawned = True
        if self.coin_count % 2 != 0 and self.spawned == True:
            self.spawned = False

        if len(self.pad) == 0:
            pass
        else:
            for pad in self.pad:
                #print(pad.x,pad.y)
                for other_pads in self.pad:
                    if other_pads == pad and len(self.pad) > 1:
                        pass

                    if pad.x > self.player.x  and (self.game.isCollision(pad.x - 1, pad.y, other_pads.x, other_pads.y, 54, 54) == False or len(self.pad) == 1):
                        pad.moveLeft()
                    elif pad.x < self.player.x and (self.game.isCollision(pad.x + 1, pad.y, other_pads.x, other_pads.y, 54, 54) == False or len(self.pad) == 1):
                        pad.moveRight(  )

                    if pad.y > self.player.y and (self.game.isCollision(pad.x, pad.y - 1, other_pads.x, other_pads.y, 54, 54) == False or len(self.pad) == 1):
                        pad.moveUp()
                    elif pad.y < self.player.y and (self.game.isCollision(pad.x, pad.y + 1, other_pads.x, other_pads.y, 54, 54) == False or len(self.pad) == 1):
                        pad.moveDown()

                if self.game.isCollision(pad.x, pad.y, self.player.x, self.player.y, 52, 52):
                    self._running = False

        pass

    def on_render(self):
        """
        Deals with rendering things on screen.
        """

        self._display_surf.fill((0, 0, 0))
        self._display_surf.blit(self._image_surf, (self.player.x, self.player.y))
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
                self.player.moveRight()

            if ((keys[K_LEFT] or keys[K_a]) and self.player.x > 0):
                self.player.moveLeft()

            if ((keys[K_UP] or keys[K_w]) and self.player.y > 0):
                self.player.moveUp()

            if ((keys[K_DOWN] or keys[K_s]) and self.player.y + 52 < self.windowHeight):
                self.player.moveDown()

            if keys[K_ESCAPE]:
                self._running = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

            self.on_loop()
            self.on_render()

        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
