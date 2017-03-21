# Imports Libraries
import pygame
import sys
from pygame.locals import *

Width = 1600
Height = 900


# Initialise Pygame
pygame.init()

# declare variable 'screen' and set the display window
screen = pygame.display.set_mode((Width, Height))


# Declare variable for image and load it into pygame
Beach = pygame.image.load('Beach.jpg')
screen.blit(Beach, (0, 0))
pygame.display.flip()
PixArray = pygame.PixelArray(screen)

def Blackandwhite():
    """ Turns image to black and white"""
    for Y in range(0, Height):
        for X in range(0, Width):

            # Gets the RGB Values of the pixel
            red = screen.get_at((X, Y)).r
            green = screen.get_at((X, Y)).g
            blue = screen.get_at((X, Y)).b
            if red + green + blue > 200:
                red = 0
                green = 0
                blue = 0
            else:
                red = 255
                green = 255
                blue = 255

            # Updates the Pixel Array
            PixArray[X, Y] = (red, green, blue)


Blackandwhite()

# Update the full display surface to the screen
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()