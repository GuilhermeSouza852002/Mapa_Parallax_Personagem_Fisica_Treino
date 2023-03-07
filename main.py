import pygame, sys
from settings import *
from level import Level

# Setup do pygame
#iniciação do jogo
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height)) 
pygame.display.set_caption('SuperMario100%Pirata') #nome do display
clock = pygame.time.Clock()

#sprite_sheet_image = pygame.image.load('personagem/Morcego32x32.png').convert_alpha()
background_image = pygame.image.load('mapa\map.jpg')    #mapa fundo

level = Level(level_map,screen) #metodo do level

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(background_image, (0, 0))   #plotando fundo do mapa
    #screen.fill('#c5efe0') #definição da cor de fundo
    level.run()

    pygame.display.update()
    clock.tick(60)