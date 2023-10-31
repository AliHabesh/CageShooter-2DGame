import pygame

from characters.shooter import Shooter

# Initialize the pygame
pygame.init()

# Create game window size
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# player = pygame.Rect((300, 250, 50, 50))


player = Shooter("assets/player_chaingun.png", 400, 300)

# Game loop
run = True
while run:
    screen.fill((0, 0, 0))

    screen.blit(player.image, player.rect)
    player.character_movement()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
