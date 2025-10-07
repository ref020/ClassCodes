import pygame
import random
from random import randint, choice
from Wizard import *
from Constants import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("spider.png").convert()
        self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (40, 40))  # Resize sprite
        self.rect = self.surf.get_rect()
        self.rect.y = random.randint(0, (int(HEIGHT/2)))#random position
        self.rect.x = 0
        self.speed = 1

    # Move the sprite based on speed
    # Remove the sprite when it passes the right side of the screen
    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.top > HEIGHT:
            self.kill()
        if self.rect.left > WIDTH + 40:
            self.kill()
