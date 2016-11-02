import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 585))
image = pygame.image.load('Lute.jpg')

sprite = pygame.sprite.Sprite()
sprite.image = image
sprite.rect = image.get_rect()

font = pygame.font.SysFont('Sans', 58)
text = font.render("Here's Wonderwall", True, (255, 255, 255))

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