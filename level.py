import pygame
from tiles import Tile
from settings import tile_size
from player import Player

class Level:
    def __init__(self,level_data,surface):
        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        
        self.world_shift = 0
     #O conjunto de X ganha forma no mapa
     
    #percorre as linhas do mapa e as númera 
    def setup_level(self,layout):   
         self.tiles = pygame.sprite.Group()     #grupo para as plataformas X
         self.player = pygame.sprite.GroupSingle()    #grupo para os players P
         
         for row_index,row in enumerate(layout):
             for col_index,cell in enumerate(row):
                 x = col_index * tile_size
                 y = row_index * tile_size
                 
                 if cell == 'X':
                    tile = Tile((x,y),tile_size) 
                    self.tiles.add(tile)
                 if cell == 'P':
                     player_sprite = Player((x,y)) 
                     self.player.add(player_sprite)
        
    def run(self):
        #desenhar o level
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        
        #desenhar o player
        self.player.update()
        self.player.draw(self.display_surface)