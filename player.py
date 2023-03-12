import pygame

#Corpo do player
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,collision_sprites):
        super().__init__(groups)
        self.image = pygame.Surface((32,64))    #tamanho player
        self.image.fill('#000000')  #cor player
        self.rect = self.image.get_rect(topleft = pos)
        
        #movimentação do player
        self.direction = pygame.math.Vector2()
        self.speed = 5                           #velocidade player
        self.gravity = 0.8                       #gravidade
        self.jump_speed = 16                     #velocidade do pulo
        self.collision_sprites = collision_sprites
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
            self.direction.y = -self.jump_speed
            
    def horizontal_movement_collision(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                elif self.direction.x > 0:
                    self.rect.right = sprite.rect.left
    
    def vertical_movement_collidion(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_floor = True
                elif self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
                
            if self.on_floor and self.direction.y != 0:
                self.on_floor =  False        
            
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.speed
        self.vertical_movement_collidion()
        self.apply_gravity()
        self.horizontal_movement_collision()
        
        