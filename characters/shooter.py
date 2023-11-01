import pygame
import math


class Shooter(pygame.sprite.Sprite):
    original_shooter = None

    def __init__(self, url, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(url)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        Shooter.original_shooter = self.image.convert_alpha()

    def character_movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.move_ip(-1, 0)
        if key[pygame.K_d]:
            self.rect.move_ip(1, 0)
        if key[pygame.K_s]:
            self.rect.move_ip(0, 1)
        if key[pygame.K_w]:
            self.rect.move_ip(0, -1)

    def character_rotation(self):
        mouse_position = pygame.mouse.get_pos()
        direction_vector = pygame.Vector2(mouse_position[0] - self.rect.centerx, self.rect.centery - mouse_position[1])

        angle = -direction_vector.angle_to(pygame.Vector2(1, 0))
        self.image = pygame.transform.rotate(Shooter.original_shooter, angle)
        self.rect = self.image.get_rect(center=self.rect.center)
