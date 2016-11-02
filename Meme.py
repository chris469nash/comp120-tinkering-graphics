import pygame
import sys
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

width = 800
height = 600

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Meme")

gameExit = False

lead_x = width/2
lead_y = height/2

lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

block_size = 10
FPS = 30

font = pygame.font.SysFont(None, 25)

def message_to_screen(msg, red):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [width/2, height/2])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
