import pygame
from random import randint, choice
from Constants import *
from Projectile import *

    

#Wizard Class, sets up surfs and keys and size of sprite
class Wizard(pygame.sprite.Sprite):
    def __init__(self):
        super(Wizard, self).__init__()
        self.surf = pygame.image.load("wizard.png").convert()#iamge of wizard
        self.surf.set_colorkey((0,0,0), pygame.RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (60, 60))  # Resize sprite
        self.rect = self.surf.get_rect()
        self.rect.x = 100#where he starts


    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-4, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(4, 0)

        self.rect.bottom = HEIGHT

        # Keeps player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    # Shoots a projectile from the player
    def shoot(self):
        new_projectile = Projectile(self.rect.centerx, self.rect.top)
        projectiles.add(new_projectile)
        all_sprites.add(new_projectile)
