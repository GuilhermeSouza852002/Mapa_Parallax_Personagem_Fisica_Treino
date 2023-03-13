import pygame
from settings import *
from tiles import Tile
from player import Player

class Level:
    def __init__(self):
        
        # level setup
        self.display_surface = pygame.display.get_surface() #obtendo a superficie
        
        # sprite group setup
        self.visible_sprites = CameraGroup() #grupo que desenha o jogo na tela
        self.active_sprites = pygame.sprite.Group() #grupo que atualiza as sprites
        self.collision_sprites = pygame.sprite.Group() #grupo das sprites que colidem 
        
        self.setup_level()
     
    #percorre as linhas do mapa e as númera 
    def setup_level(self):   
         #descobrindo a posição x e y dos ladrilhos
         for row_index,row in enumerate(level_map):	#lendo linha por linha do level_map horizontal
             for col_index,cell in enumerate(row):	#lendo colunas na vertical
                 x = col_index * tile_size #obtendo a posição de x
                 y = row_index * tile_size #obtendo a posição de y
                 
                 if cell == 'X':        #se a celula/coluna for igual a X ela recebe X que é a estrutura do mapa
                    Tile((x,y),[self.visible_sprites,self.collision_sprites])	#colocando a estrutura do mapa na posição
                 if cell == 'P':        #se a celula/coluna for igual a P ela recebe P que é o player
                    self.player = Player((x,y),[self.visible_sprites,self.active_sprites],self.collision_sprites) #colocando jogador na posição

                    
    def run(self):
        #desenhar o level
        # run the entire game (level)
        self.active_sprites.update()
        self.visible_sprites.custom_draw(self.player)

class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.offset = pygame.math.Vector2(100,300)

		# center camera setup 
		# self.half_w = self.display_surface.get_size()[0] // 2
		# self.half_h = self.display_surface.get_size()[1] // 2

		# camera
		cam_left = CAMERA_BORDERS['left']
		cam_top = CAMERA_BORDERS['top']
		cam_width = self.display_surface.get_size()[0] - (cam_left + CAMERA_BORDERS['right'])
		cam_height = self.display_surface.get_size()[1] - (cam_top + CAMERA_BORDERS['bottom'])

		self.camera_rect = pygame.Rect(cam_left,cam_top,cam_width,cam_height)

	def custom_draw(self,player):

		# get the player offset 
		# self.offset.x = player.rect.centerx - self.half_w
		# self.offset.y = player.rect.centery - self.half_h

		# getting the camera position
		if player.rect.left < self.camera_rect.left:
			self.camera_rect.left = player.rect.left
		if player.rect.right > self.camera_rect.right:
			self.camera_rect.right = player.rect.right
		if player.rect.top < self.camera_rect.top:
			self.camera_rect.top = player.rect.top
		if player.rect.bottom > self.camera_rect.bottom:
			self.camera_rect.bottom = player.rect.bottom

		# camera offset 
		self.offset = pygame.math.Vector2(
			self.camera_rect.left - CAMERA_BORDERS['left'],
			self.camera_rect.top - CAMERA_BORDERS['top'])

		for sprite in self.sprites():
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)