import pygame
import sys
from pygame.locals import *

pygame.init()


screen = pygame.display.set_mode((400, 585))
image = pygame.image.load('Faceswap.jpg')


font = pygame.font.SysFont('Sans', 38)
text = font.render("When a simple faceswap", True, (255, 255, 255))
text2 = font.render("Creates two monsters", True, (255, 255, 255))
screen.blit(image, (0, 0))
screen.blit(text, (0, 0))
screen.blit(text2, (39, 500))


pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()