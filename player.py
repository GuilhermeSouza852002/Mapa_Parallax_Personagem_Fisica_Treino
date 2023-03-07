import pygame

#Corpo do player
class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((32,64))    #tamanho player
        self.image.fill('#0bf246')  #cor player
        self.rect = self.image.get_rect(topleft = pos)
        
        #movimentação do player
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5                           #velocidade player
        self.gravity = 0.8
        self.jump_speed = -16
        self.on_floor = False
        
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]: #direita
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:  #esquerda
            self.direction.x = -1
        else:
            self.direction.x = 0
            
        if keys[pygame.K_SPACE] and self.on_floor:  #pulo, limitação de pulo
            self.jump()
            
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def jump(self):
        self.direction.y = self.jump_speed
    
    def update(self):
        self.get_input()