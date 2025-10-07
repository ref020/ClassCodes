import pygame
from Constants import *
from Wizard import *
from Enemy import *


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Projectile, self).__init__()
        self.surf = pygame.image.load("fireball.png").convert()
        self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (20, 20))  # Resize sprite
        self.rect = self.surf.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    # Moves the fireball/sprite upwards
    def update(self):
        self.rect.move_ip(0, -1)
        if self.rect.bottom < 0:
            self.kill()
            # Check for collisions with enemies
            hits = pygame.sprite.spritecollide(self, enemies, True)
            for hit in hits:
                hit.kill()
        
