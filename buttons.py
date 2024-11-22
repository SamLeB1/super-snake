import pygame
import maps
import settings
import text


class IncrementDecrement(pygame.sprite.Sprite):
    def __init__(self, identifier):
        pygame.sprite.Sprite.__init__(self)

        self.identifier = identifier
        if identifier == 0:
            self.image = pygame.image.load("assets/sprites/increment.png")
            self.old_image = pygame.image.load("assets/sprites/increment.png")
            self.rect = self.image.get_rect()
            self.rect.midtop = ((settings.screen_width / 2) + 24, (settings.screen_height * 0.75) + 48)
            self.old_rect = self.rect
            self.size = self.image.get_size()
            self.center = self.rect.center
        elif identifier == 1:
            self.image = pygame.image.load("assets/sprites/decrement.png")
            self.old_image = pygame.image.load("assets/sprites/decrement.png")
            self.rect = self.image.get_rect()
            self.rect.midtop = ((settings.screen_width / 2) - 24, (settings.screen_height * 0.75) + 48)
            self.old_rect = self.rect
            self.size = self.image.get_size()
            self.center = self.rect.center

    def click(self):
        if self.identifier == 0:
            if text.snake_speed.speed < 10:
                text.snake_speed.speed += 1
        elif self.identifier == 1:
            if text.snake_speed.speed > 1:
                text.snake_speed.speed -= 1

    def resize_image(self):
        self.image = pygame.transform.scale(self.image, (self.size[0] * 0.9, self.size[1] * 0.9))
        self.rect = self.image.get_rect()
        self.rect.center = self.center

    def revert_image(self):
        self.image = self.old_image
        self.rect = self.image.get_rect()
        if self.identifier == 0:
            self.rect.midtop = ((settings.screen_width / 2) + 24, (settings.screen_height * 0.75) + 48)
        elif self.identifier == 1:
            self.rect.midtop = ((settings.screen_width / 2) - 24, (settings.screen_height * 0.75) + 48)

    def update(self, events):
        if self.old_rect.collidepoint(pygame.mouse.get_pos()):
            self.resize_image()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    state = pygame.mouse.get_pressed()
                    if state[0]:
                        self.click()
        else:
            self.revert_image()


class Arrow(pygame.sprite.Sprite):
    def __init__(self, identifier):
        pygame.sprite.Sprite.__init__(self)

        self.identifier = identifier
        if identifier == 0:
            self.image = pygame.image.load("assets/sprites/arrow_left.png")
            self.old_image = pygame.image.load("assets/sprites/arrow_left.png")
            self.rect = self.image.get_rect()
            self.rect.midtop = ((settings.screen_width / 2) - 24, (settings.screen_height * 0.75) - 32)
            self.old_rect = self.rect
            self.size = self.image.get_size()
            self.center = self.rect.center
        elif identifier == 1:
            self.image = pygame.image.load("assets/sprites/arrow_right.png")
            self.old_image = pygame.image.load("assets/sprites/arrow_right.png")
            self.rect = self.image.get_rect()
            self.rect.midtop = ((settings.screen_width / 2) + 24, (settings.screen_height * 0.75) - 32)
            self.old_rect = self.rect
            self.size = self.image.get_size()
            self.center = self.rect.center

    def click(self):
        if self.identifier == 0:
            if maps.maps.selected_map_index > 0:
                maps.maps.selected_map_index -= 1
            else:
                maps.maps.selected_map_index = len(maps.maps.maps) - 1

            if maps.maps.selected_map_index == 0:
                maps.maps.random_is_selected = True
            else:
                maps.maps.random_is_selected = False

        elif self.identifier == 1:
            if maps.maps.selected_map_index < len(maps.maps.maps) - 1:
                maps.maps.selected_map_index += 1
            else:
                maps.maps.selected_map_index = 0

            if maps.maps.selected_map_index == 0:
                maps.maps.random_is_selected = True
            else:
                maps.maps.random_is_selected = False

    def resize_image(self):
        self.image = pygame.transform.scale(self.image, (self.size[0] * 0.9, self.size[1] * 0.9))
        self.rect = self.image.get_rect()
        self.rect.center = self.center

    def revert_image(self):
        self.image = self.old_image
        self.rect = self.image.get_rect()
        if self.identifier == 0:
            self.rect.midtop = ((settings.screen_width / 2) - 24, (settings.screen_height * 0.75) - 32)
        elif self.identifier == 1:
            self.rect.midtop = ((settings.screen_width / 2) + 24, (settings.screen_height * 0.75) - 32)

    def update(self, events):
        if self.old_rect.collidepoint(pygame.mouse.get_pos()):
            self.resize_image()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    state = pygame.mouse.get_pressed()
                    if state[0]:
                        self.click()
        else:
            self.revert_image()


increment = IncrementDecrement(0)
decrement = IncrementDecrement(1)
increment_decrement_group = pygame.sprite.Group()
increment_decrement_group.add(increment, decrement)

arrow_left = Arrow(0)
arrow_right = Arrow(1)
arrow_group = pygame.sprite.Group()
arrow_group.add(arrow_left, arrow_right)
