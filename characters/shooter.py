import pygame


class Shooter(pygame.sprite.Sprite):
    def __init__(self, url, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(url)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

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
