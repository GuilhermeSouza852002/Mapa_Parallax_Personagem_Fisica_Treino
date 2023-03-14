import pygame, sys
from settings import *
from level import Level

# Setup do pygame
#iniciação do jogo
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height)) #Definindo a janela de exibição
pygame.display.set_caption('SuperMario100%Pirata') #nome do display
clock = pygame.time.Clock()

#sprite_sheet_image = pygame.image.load('personagem/Morcego32x32.png').convert_alpha()
#background_image = pygame.image.load('mapa\map.jpg')    #mapa fundo
#variaveis de rolagem parallax
scroll = 0 

ground_image = pygame.image.load("mapa/ground.png").convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

background_images = []
for i in range(1,6):
    background_image = pygame.image.load(f"mapa/plx-{i}.png").convert_alpha()
    background_images.append(background_image)  #carregando a lista das imagens de fundo
background_width = background_images[0].get_width() #pegando a largura real da imagem

def draw_bg():  #desenhado na tela
    for x in range(20):
        speed = 1
        for i in background_images:
            screen.blit(i, ((x * background_width) - scroll * speed, 0))
            speed += 0.1
            
level = Level() 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #screen.blit(background_image, (0, 0))   #plotando fundo do mapa
    #screen.fill('#c5efe0') #definição da cor de fundo
    draw_bg()
    
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and scroll > 0:
        scroll -= 5
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] and scroll < 6000:
        scroll += 5
        
    def draw_ground():
        for x in range(50):
            screen.blit(ground_image, ((x * ground_width) - scroll * 1.5, screen_height - ground_height))
    
    draw_ground()        
    level.run()

    pygame.display.update()
    clock.tick(fps)