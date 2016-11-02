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

sprite = pygame.sprite.Sprite()
sprite.image = image
sprite.rect = image.get_rect()

font = pygame.font.SysFont('Sans', 38)
text = font.render("When Your Phone Runs Out", True, (255, 255, 255))
#screen.blit (text,[,])

sprite.image.blit(text, sprite.rect)

group = pygame.sprite.Group()
group.add(sprite)
group.draw(screen)

pygame.display.flip()

print 'bits per pixel:'
print 'image', image.get_bitsize()
print 'screen', screen.get_bitsize()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()