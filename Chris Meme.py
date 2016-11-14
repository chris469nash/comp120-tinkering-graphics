import pygame
import sys
from pygame.locals import *

pygame.init()


screen = pygame.display.set_mode((400, 585))
image = pygame.image.load('Sweet dreams.jpg')


font = pygame.font.SysFont('Sans', 38)
text = font.render("Did you have", True, (255, 255, 255))
text2 = font.render("Sweet dreams?", True, (255, 255, 255))
screen.blit(image, (0, 0))
screen.blit(text, (0, 0))
screen.blit(text2, (39, 500))


pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()