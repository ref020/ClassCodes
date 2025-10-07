#####################################################################
#   File containing constants that you might need in your assignment.
#   Make sure to import the library in all your files using a statement
#   like:
#   from Constants import *
#####################################################################

# import libraries that you will need
import pygame
from random import randint, choice


pygame.init()
 
#groups

enemies = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

 

# constants for screen size
WIDTH = 1100
HEIGHT = 800

# constants for colors
RED = [0xe3, 0x1b, 0x23]
BLUE = [0x00,0x2F,0x8B]
GREY = [0xA2, 0xAA, 0xAD]
WHITE = [0xFF, 0xFF, 0xFF]
BLACK = [0x00, 0x00, 0x00]
GREEN = [0x00, 0xFF, 0x00]

COLORS = [BLUE, RED, GREY, WHITE, BLACK]

FPS = 60
FramePerSec = pygame.time.Clock()
 
DISPLAYSURF = pygame.display.set_mode((600,800))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
# keys from pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE,
)
