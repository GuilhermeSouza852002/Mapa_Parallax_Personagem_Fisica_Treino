import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.Surface((tile_size,tile_size))
        #self.image.fill('#65220d')
        texture = pygame.image.load('mapa/bloco.png').convert()    #mapa fundo
        self.image.blit(texture, (0, 0))
        self.rect = self.image.get_rect(topleft = pos)