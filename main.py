import pygame

# Initialize the pygame
pygame.init()

# Create game window size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))


def character_movement():
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-1, 0)
    if key[pygame.K_d]:
        player.move_ip(1, 0)
    if key[pygame.K_s]:
        player.move_ip(0, 1)
    if key[pygame.K_w]:
        player.move_ip(0, -1)


# Game loop
run = True
while run:
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player)
    character_movement()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
