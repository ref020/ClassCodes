import pygame
import sys
from random import randint, choice
from Wizard import *
from Constants import *
from Enemy import*



########################### main game################################

# Initialize pygame
pygame.init()

#Creates Screen Caption and size
# The size is determined by the constant WIDTH and HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shoot the spider... Reloaded")

def start_menu():
    # Creates font for text and text itself
    font = pygame.font.SysFont(None, 48)
    text = font.render("Press Start to Play", True, BLACK)

    #Center text on screen
    game_on_text = font.render("Start Game", True, BLACK)

    game_on_text_rect = game_on_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

    # Draw the starting menu
    screen.fill(GREY)
    screen.blit(game_on_text, game_on_text_rect)

    # Draw the "Play" button
    game_on_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 100, 100, 50)
    pygame.draw.rect(screen, GREEN, game_on_rect)

    #updates game
    pygame.display.flip()

    # Wait for user input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if game_on_rect.collidepoint(event.pos):
                    return  # Return to game loop if start button is clicked



# Create the ending menu
def end_menu(s):
    font = pygame.font.SysFont(None, 48)
    #Create the Game Over, Score, and Try Again texts and sets up font above ^
    game_over_text = font.render("Game Over", True, BLACK)
    try_again_text = font.render("Try Again", True, BLACK)
    score_text = font.render(f"Score:{s}", True, BLUE)


    game_over_text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    try_again_text_rect = try_again_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    score_text_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    #Makes ending menu
    screen.fill(GREY)
    screen.blit(game_over_text, game_over_text_rect)
    screen.blit(try_again_text, try_again_text_rect)
    screen.blit(score_text, score_text_rect)

    # Makes "Try Again" button
    try_again_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 100, 100, 50)
    pygame.draw.rect(screen, GREEN, try_again_rect)

    pygame.display.flip()

    # Waits for user click
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if try_again_rect.collidepoint(event.pos):
                    for enemy in enemies:
                        enemy.kill()
                    return start_menu()# Restart the game

start_menu()

#Adds new enemys
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1000)
#Instantiate player
player = Wizard()

all_sprites.add(player)



#score is for counting enemys killed
score = 0
#life is for counting how many lifes before game ends
lives = 5

# Run the game loop
running = True


#############################MAIN LOOP####################

while running:
    # Handles different events, shoot(space bar is last)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()  # Call shoot() method when space is called

    # Get the state of all pressed keys
    pressed_keys = pygame.key.get_pressed()

    #Updates player
    player.update(pressed_keys)

    #Updates projectiles
    projectiles.update()

    #Updates enemies
    enemies.update()

    #Checks for collisions between projectiles and enemies
    #Checks for collisions between projectiles and enemies
    hits = pygame.sprite.groupcollide(projectiles, enemies, True, True)
    for hit in hits:
        score += 1  # Increase score by 1 for every enemy killed

    for enemy in enemies:
        if enemy.rect.right >= WIDTH + 40:
            enemies.remove(enemy)
            if lives > 0:
                lives -= 1
            if lives == 0:
                end_menu(score)
                lives = 5
                score = 0
                

    #Draw background
    screen.fill(BLACK)

    #Draw sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    #Draw score display
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(text, (10, 10))

    #Draw life display
    font = pygame.font.Font(None, 36)
    text = font.render(f"Lives: {lives}", True, RED)
    screen.blit(text, (110, 10))

    #Update display
    pygame.display.flip()

#Quit pygame
pygame.quit()

