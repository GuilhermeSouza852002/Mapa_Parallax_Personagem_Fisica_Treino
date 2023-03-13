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

#camera que se move como jogador
class CameraGroup(pygame.sprite.Group):	#herdando sprite.Group
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()	#estamos dando ao CameraGroup o que queremos desenhar, assim não á necessidade de passar nenhum argumento para custom_draw
		self.offset = pygame.math.Vector2(100,300) #posição superior a esquerda x e y

		# camera
  		# devemos pegar a posição e o tamanho do retângulo
		cam_left = CAMERA_BORDERS['left']	#cria uma borda do tamanho que foi definido o left
		cam_top = CAMERA_BORDERS['top']		#cria uma borda do tamanho que foi definido o top
		#descobrindo a altura e a lagurar do retângulo
		cam_width = self.display_surface.get_size()[0] - (cam_left + CAMERA_BORDERS['right'])	#subtrai a largura total da tela left e right pra gerar a borda da tela da nova largura
		cam_height = self.display_surface.get_size()[1] - (cam_top + CAMERA_BORDERS['bottom'])	#subtrai a autura total da tela top e bottom pra gerar a borda da tela da nova autura

		self.camera_rect = pygame.Rect(cam_left,cam_top,cam_width,cam_height) #pegando a camera que sera movida pelo jogador

	def custom_draw(self,player):
     	# movendo a camera
		if player.rect.left < self.camera_rect.left:	#o player esta mais para a esquerda da camera
			self.camera_rect.left = player.rect.left	#então a camera é destruida e jogada para a esquerda
		if player.rect.right > self.camera_rect.right:	#o player esta mais para a direita da camera
			self.camera_rect.right = player.rect.right	#então a camera é destruida e jogada para a direita
		if player.rect.top < self.camera_rect.top:		#o player esta mais para cima da camera
			self.camera_rect.top = player.rect.top		#então a camera é destruida e jogada para cima
		if player.rect.bottom > self.camera_rect.bottom:#o player esta mais para baixo da camera
			self.camera_rect.bottom = player.rect.bottom#então a camera é destruida e jogada para baixo

		# camera offset 
		# deslocamento da camera
		self.offset = pygame.math.Vector2(
      	# pegando a posição superior esquerda da tela para que o jogador sempre esteja no centro da tela	
			self.camera_rect.left - CAMERA_BORDERS['left'],
			self.camera_rect.top - CAMERA_BORDERS['top'])

		for sprite in self.sprites():	#replicando todos os elementos na tela
			offset_pos = sprite.rect.topleft - self.offset #posição de deslocamento automatico
			self.display_surface.blit(sprite.image,offset_pos) #desenhado todos os elementos na tela