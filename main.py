import pygame
from pygame.time import Clock

from characters.shooter import Shooter
from map.game_map import Map

pygame.init()

# Game window size
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 704
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cage Shooter")

# Load the game logo
game_logo = pygame.image.load("assets/CageShooterLogo.jpg")
pygame.display.set_icon(game_logo)

# Create a Shooter object
player = Shooter("assets/player_chaingun.png", 500, 300, width=640, height=360)
collision_list = ["Walls", "collision"]

# Load game map
game_map = Map("assets/CageShooterMap.tmx", collision_list)
clock = Clock()
print(game_map.map.layers)
# Game loop
run = True
while run:
    dt = clock.tick(180) / 1000
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Draw the game map
    for layer in game_map.map.visible_layers:
        if layer.name == "aboveCharacter":
            screen.blit(player.image, player.rect)
        for x, y, gid in layer:
            tile = game_map.map.get_tile_image_by_gid(gid)
            if tile is not None:
                screen.blit(tile, (x * game_map.map.tilewidth, y * game_map.map.tileheight))

    # Character movement and rotation
    center_rect = pygame.Rect(player.rect.centerx - 5, player.rect.centery - 5, 10, 10)
    player.character_movement(game_map.collision_sprites)
    player.character_rotation()

    pygame.display.update()

pygame.quit()
