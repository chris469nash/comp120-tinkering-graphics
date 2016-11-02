import pygame
import sys
import time
from pygame.locals import *

pygame.init()

Width = 400
Height = 585

BLACK = (0, 0, 0)

screen = pygame.display.set_mode((400, 585))
image = pygame.image.load('Jesus.jpg')

a = 100
b = 200


font = pygame.font.SysFont('Sans', 38)
text = font.render("When Your Phone Runs Out", True, (255, 255, 255))
text2 = font.render("In a Lecture", True, (255, 255, 255))
screen.blit(image, (0, 0))
screen.blit(text,(0, 0))
screen.blit(text2,(115, 500))


pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()