import pygame
import math


class Shooter(pygame.sprite.Sprite):
    original_shooter = None

    def __init__(self, url, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(url)
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.center = (x, y)
        Shooter.original_shooter = self.image.convert_alpha()

    def character_movement(self, collision_sprites):
        key = pygame.key.get_pressed()
        new_rect = self.rect.copy()

        if key[pygame.K_a]:
            new_rect.move_ip(-1, 0)
        if key[pygame.K_d]:
            new_rect.move_ip(1, 0)
        if key[pygame.K_s]:
            new_rect.move_ip(0, 1)
        if key[pygame.K_w]:
            new_rect.move_ip(0, -1)

        new_center = new_rect.center

        for tile in collision_sprites:

            if (
                    tile.rect.left <= new_center[0] <= tile.rect.right
                    and tile.rect.top <= new_center[1] <= tile.rect.bottom
            ):
                return

        self.rect = new_rect

    def character_rotation(self):
        mouse_position = pygame.mouse.get_pos()
        direction_vector = pygame.Vector2(mouse_position[0] - self.rect.centerx, self.rect.centery - mouse_position[1])
        angle = -direction_vector.angle_to(pygame.Vector2(1, 0))
        self.image = pygame.transform.rotate(Shooter.original_shooter, angle)
        self.rect = self.image.get_rect(center=self.rect.center)
