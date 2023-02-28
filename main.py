import pygame, sys
from settings import *
from level import Level

# Setup do pygame
#iniciação do jogo
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height)) 
pygame.display.set_caption('SuperMario100%Pirata') #nome do display
clock = pygame.time.Clock()

level = Level(level_map,screen) #metodo do level

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('black') #definição da cor de fundo
    level.run()
    
    pygame.display.update()
    clock.tick(60)