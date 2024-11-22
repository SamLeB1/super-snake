import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("assets/sprites/background.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (-80, 0)
        self.offset = -80

    def reset(self):
        self.offset = -80
        self.rect.topleft = (-80, 0)

    def update(self):
        self.offset += 0.5
        self.rect.left = self.offset
        if self.offset >= 0:
            self.offset = -80


background = Background()
background_group = pygame.sprite.Group()
background_group.add(background)
