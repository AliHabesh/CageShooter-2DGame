from pytmx.util_pygame import load_pygame
import pygame


class Map:
    def __init__(self, url, collisition_list):
        self.map = load_pygame("assets/CageShooterMap.tmx")
        self.collision_list = ["Walls", "collision"]
        self.collision_sprites = pygame.sprite.Group()

        self._create_collision_sprites()

    def _create_collision_sprites(self):
        for layer in self.map.visible_layers:
            if layer.name in self.collision_list:
                for x, y, gid in layer:
                    tile_image = self.map.get_tile_image_by_gid(gid)
                    if tile_image is not None:
                        tile_sprite = pygame.sprite.Sprite()
                        tile_sprite.image = tile_image
                        tile_sprite.rect = tile_image.get_rect()
                        tile_sprite.rect.topleft = (x * self.map.tilewidth, y * self.map.tileheight)
                        self.collision_sprites.add(tile_sprite)

