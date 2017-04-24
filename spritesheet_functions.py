"""
This module is used for individual sprites to be pulled from sprite sheets.
"""

import pygame

class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """

    def __init__(self, file_name):
        """ Constructor; pass in the file name of the sprite sheet. """

        # Load the image into sprite_sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()

    def get_image(self, x, y, width, height, colorkey=None):
        """
        Grab a single image out of a larger sprite sheet.
        Pass in the x and y location of the sprite, along
        with the width and height of the sprite.

        Color key is the tuple that contains R, G, B values of
        what color is used as a key.
        """

        # Create a new blank image.
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image.
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assume the last argument  is the transparent color.
        image.set_colorkey(colorkey)

        # Serve up the image.
        return image
