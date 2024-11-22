import pygame
from game import game
import maps
import settings


class Countdown(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = font.render("3...", True, "white")
        self.rect = self.image.get_rect()
        self.rect.center = (settings.screen_width / 2, settings.screen_height / 2)

    def update(self):
        if game.state == "active" or game.state == "active_2p":
            if pygame.time.get_ticks() - play_again.static_time < 1000:
                self.image = font.render("3...", True, "white")
                opacity = int((1000 - (pygame.time.get_ticks() - play_again.static_time - 0)) / 2)
                self.image.set_alpha(opacity)
                self.rect = self.image.get_rect()
                self.rect.center = (settings.screen_width / 2, settings.screen_height / 2)

            elif pygame.time.get_ticks() - play_again.static_time < 2000:
                self.image = font.render("2...", True, "white")
                opacity = int((1000 - (pygame.time.get_ticks() - play_again.static_time - 1000)) / 2)
                self.image.set_alpha(opacity)
                self.rect = self.image.get_rect()
                self.rect.center = (settings.screen_width / 2, settings.screen_height / 2)

            elif pygame.time.get_ticks() - play_again.static_time < 3000:
                self.image = font.render("1...", True, "white")
                opacity = int((1000 - (pygame.time.get_ticks() - play_again.static_time - 2000)) / 2)
                self.image.set_alpha(opacity)
                self.rect = self.image.get_rect()
                self.rect.center = (settings.screen_width / 2, settings.screen_height / 2)

            elif pygame.time.get_ticks() - play_again.static_time < 4000:
                self.image = font.render("Go!", True, "white")
                opacity = int((1000 - (pygame.time.get_ticks() - play_again.static_time - 3000)) / 2)
                self.image.set_alpha(opacity)
                self.rect = self.image.get_rect()
                self.rect.center = (settings.screen_width / 2, settings.screen_height / 2)
            else:
                self.image = font.render("", True, "white")
                self.rect = self.image.get_rect()
                self.rect.center = (settings.screen_width / 2, settings.screen_height / 2)

        elif game.state == "active_cpu":
            if pygame.time.get_ticks() - play_cpu.static_time < 1000:
                self.image = font.render("3...", True, "white")
                opacity = int((1000 - (pygame.time.get_ticks() - play_cpu.static_time - 0)) / 2)
                self.image.set_alpha(opacity)
                self.rect = self.image.get_rect()
                self.rect.center = (settings.screen_width / 2, settings.screen_height / 2)

            elif pygame.time.get_ticks() - play_cpu.static_time < 2000:
                self.image = font.render("2...", True, "white")
                opacity = int((1000 - (pygame.time.get_ticks() - play_cpu.static_time - 1000)) / 2)
                self.image.set_alpha(opacity)
                self.rect = self.image.get_rect()
                self.rect.center = (settings.screen_width / 2, settings.screen_height / 2)

            elif pygame.time.get_ticks() - play_cpu.static_time < 3000:
                self.image = font.render("1...", True, "white")
                opacity = int((1000 - (pygame.time.get_ticks() - play_cpu.static_time - 2000)) / 2)
                self.image.set_alpha(opacity)
                self.rect = self.image.get_rect()
                self.rect.center = (settings.screen_width / 2, settings.screen_height / 2)

            elif pygame.time.get_ticks() - play_cpu.static_time < 4000:
                self.image = font.render("Go!", True, "white")
                opacity = int((1000 - (pygame.time.get_ticks() - play_cpu.static_time - 3000)) / 2)
                self.image.set_alpha(opacity)
                self.rect = self.image.get_rect()
                self.rect.center = (settings.screen_width / 2, settings.screen_height / 2)
            else:
                self.image = font.render("", True, "white")
                self.rect = self.image.get_rect()
                self.rect.center = (settings.screen_width / 2, settings.screen_height / 2)


class HighScore(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.high_score = 0
        self.image = font.render(f"High score: {self.high_score}", True, "white")
        self.rect = self.image.get_rect()
        self.rect.midtop = (settings.screen_width / 2, 64)

    def update(self):
        if game.state == "inactive":
            if score.score > self.high_score:
                self.high_score = score.score
        self.image = font.render(f"High score: {self.high_score}", True, "white")
        self.rect = self.image.get_rect()
        self.rect.midtop = (settings.screen_width / 2, 64)


class MapMessage(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.offset = -32
        self.image = font_small.render(f"", True, "white")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (settings.screen_width / 2, settings.screen_height - self.offset)

    def update(self):
        if game.state == "active" or game.state == "active_2p":
            self.image = font_small.render(f"Now playing: {maps.maps.maps[maps.maps.selected_map_index]}",
                                           True, "white")
            self.rect = self.image.get_rect()
            self.rect.midbottom = (settings.screen_width / 2, settings.screen_height - self.offset)

            if pygame.time.get_ticks() - play_again.static_time < 2000:
                self.offset += 2
                if self.offset >= 16:
                    self.offset = 16
            elif pygame.time.get_ticks() - play_again.static_time > 2000:
                self.offset -= 2
                if self.offset <= -32:
                    self.offset = -32

        elif game.state == "active_cpu":
            self.image = font_small.render(f"Now playing: {maps.maps.maps[maps.maps.selected_map_index]}",
                                           True, "white")
            self.rect = self.image.get_rect()
            self.rect.midbottom = (settings.screen_width / 2, settings.screen_height - self.offset)

            if pygame.time.get_ticks() - play_cpu.static_time < 2000:
                self.offset += 2
                if self.offset >= 16:
                    self.offset = 16
            elif pygame.time.get_ticks() - play_cpu.static_time > 2000:
                self.offset -= 2
                if self.offset <= -32:
                    self.offset = -32


class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.score = len(game.snake) - 1
        self.image = font.render(str(self.score), True, "white")
        self.rect = self.image.get_rect()
        self.rect.midtop = (settings.screen_width / 2, 16)

    def update(self):
        if game.state == "active":
            self.score = len(game.snake) - 1
            self.image = font.render(str(self.score), True, "white")
            self.rect = self.image.get_rect()
            self.rect.midtop = (settings.screen_width / 2, 16)
        elif game.state == "inactive":
            self.image = font.render(f"Score: {self.score}", True, "white")
            self.rect = self.image.get_rect()
            self.rect.midtop = (settings.screen_width / 2, 16)


class PlayerCount(pygame.sprite.Sprite):
    def __init__(self, identifier):
        pygame.sprite.Sprite.__init__(self)

        self.identifier = identifier
        if identifier == 0:
            self.image = font_small.render("One player", True, "white")
            self.rect = self.image.get_rect()
            self.rect.midbottom = (settings.screen_width / 4, settings.screen_height - 16)
            self.is_selected = True
        elif identifier == 1:
            self.image = font_small.render("Two players", True, "white")
            self.rect = self.image.get_rect()
            self.rect.midbottom = (settings.screen_width * 0.75, settings.screen_height - 16)
            self.is_selected = False

    def update(self, events):
        if self.identifier == 0:
            if self.is_selected:
                self.image = font_small.render("One player", True, "lightgray")
                return
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.image = font_small.render("One player", True, "yellow")
            else:
                self.image = font_small.render("One player", True, "white")
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.is_selected = True
                    two_players.is_selected = False
        elif self.identifier == 1:
            if self.is_selected:
                self.image = font_small.render("Two players", True, "lightgray")
                return
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.image = font_small.render("Two players", True, "yellow")
            else:
                self.image = font_small.render("Two players", True, "white")
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.is_selected = True
                    one_player.is_selected = False


class PlayAgain(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.static_time = 0
        self.image = font.render("Play", True, "white")
        self.rect = self.image.get_rect()
        self.rect.center = (settings.screen_width / 2, settings.screen_height * 0.375)

    def update(self, events):
        if game.state == "active":
            self.image = font.render("Play", True, "white")
            self.rect = self.image.get_rect()
            self.rect.center = (settings.screen_width / 2, settings.screen_height * 0.375)
        if game.state == "active_2p" or game.state == "active_cpu":
            self.image = font.render("Play vs player", True, "white")
            self.rect = self.image.get_rect()
            self.rect.midbottom = (settings.screen_width / 2, (settings.screen_height * 0.375) - 16)

        if game.state == "start" or game.state == "inactive":
            if one_player.is_selected:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.image = font.render("Play", True, "yellow")
                    self.rect = self.image.get_rect()
                    self.rect.center = (settings.screen_width / 2, settings.screen_height * 0.375)
                else:
                    self.image = font.render("Play", True, "white")
                    self.rect = self.image.get_rect()
                    self.rect.center = (settings.screen_width / 2, settings.screen_height * 0.375)
            elif two_players.is_selected:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.image = font.render("Play vs player", True, "yellow")
                    self.rect = self.image.get_rect()
                    self.rect.midbottom = (settings.screen_width / 2, (settings.screen_height * 0.375) - 16)
                else:
                    self.image = font.render("Play vs player", True, "white")
                    self.rect = self.image.get_rect()
                    self.rect.midbottom = (settings.screen_width / 2, (settings.screen_height * 0.375) - 16)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(pygame.mouse.get_pos()):
                state = pygame.mouse.get_pressed()
                if state[0]:
                    if one_player.is_selected:
                        score.score = 0
                        win_message.identifier = 0
                        self.static_time = pygame.time.get_ticks()
                        win_message.update()
                        game.state = "active"
                        game.init()
                    elif two_players.is_selected:
                        score.score = 0
                        win_message.identifier = 0
                        self.static_time = pygame.time.get_ticks()
                        score.update()
                        game.state = "active_2p"
                        game.init()


class PlayCPU(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.static_time = 0
        self.image = font.render("Play vs CPU", True, "white")
        self.rect = self.image.get_rect()
        self.rect.midtop = (settings.screen_width / 2, (settings.screen_height * 0.375) + 16)

    def update(self, events):
        if game.state == "start" or game.state == "inactive":
            if two_players.is_selected:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.image = font.render("Play vs CPU", True, "yellow")
                    self.rect = self.image.get_rect()
                    self.rect.midtop = (settings.screen_width / 2, (settings.screen_height * 0.375) + 16)
                else:
                    self.image = font.render("Play vs CPU", True, "white")
                    self.rect = self.image.get_rect()
                    self.rect.midtop = (settings.screen_width / 2, (settings.screen_height * 0.375) + 16)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(pygame.mouse.get_pos()):
                state = pygame.mouse.get_pressed()
                if state[0]:
                    if two_players.is_selected:
                        score.score = 0
                        win_message.identifier = 0
                        self.static_time = pygame.time.get_ticks()
                        score.update()
                        game.state = "active_cpu"
                        game.init()


class SnakeSpeed(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.speed = 5
        self.image = font_small.render(f"Snake speed: {self.speed}", True, "white")
        self.rect = self.image.get_rect()
        self.rect.midtop = (settings.screen_width / 2, (settings.screen_height * 0.75) + 16)

    def update(self):
        self.image = font_small.render(f"Snake speed: {self.speed}", True, "white")
        self.rect = self.image.get_rect()
        self.rect.midtop = (settings.screen_width / 2, (settings.screen_height * 0.75) + 16)


class Title(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = self.image = font_big.render("Super Snake", True, "white")
        self.rect = self.image.get_rect()
        self.rect.midtop = (settings.screen_width / 2, 16)


class WinMessage(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.identifier = 0
        self.image = font.render("", True, "white")
        self.rect = self.image.get_rect()

    def update(self):
        if self.identifier == 0:
            self.image = font.render("", True, "white")
        elif self.identifier == 1:
            self.image = font.render("Blue wins!", True, "white")
            self.rect = self.image.get_rect()
            self.rect.midtop = (settings.screen_width / 2, 64)
        elif self.identifier == 2:
            self.image = font.render("Pink wins!", True, "white")
            self.rect = self.image.get_rect()
            self.rect.midtop = (settings.screen_width / 2, 64)
        elif self.identifier == 3:
            self.image = font.render("Draw", True, "white")
            self.rect = self.image.get_rect()
            self.rect.midtop = (settings.screen_width / 2, 64)


class Wins(pygame.sprite.Sprite):
    def __init__(self, identifier):
        pygame.sprite.Sprite.__init__(self)

        self.identifier = identifier
        if identifier == 0:
            self.image = font.render(f"Blue: {game.blue_wins}", True, "white")
            self.rect = self.image.get_rect()
            self.rect.midtop = (settings.screen_width / 4, 16)
        elif identifier == 1:
            self.image = font.render(f"Pink: {game.blue_wins}", True, "white")
            self.rect = self.image.get_rect()
            self.rect.midtop = (settings.screen_width * 0.75, 16)

    def update(self):
        if self.identifier == 0:
            self.image = font.render(f"Blue: {game.blue_wins}", True, "white")
            self.rect = self.image.get_rect()
            self.rect.midtop = (settings.screen_width / 4, 16)
        elif self.identifier == 1:
            self.image = font.render(f"Pink: {game.pink_wins}", True, "white")
            self.rect = self.image.get_rect()
            self.rect.midtop = (settings.screen_width * 0.75, 16)


pygame.font.init()
font = pygame.font.Font("assets/fonts/PublicPixel-z84yD.ttf", 32)
font_big = pygame.font.Font("assets/fonts/PublicPixel-z84yD.ttf", 40)
font_small = pygame.font.Font("assets/fonts/PublicPixel-z84yD.ttf", 24)

countdown = Countdown()
countdown_group = pygame.sprite.Group()
countdown_group.add(countdown)

score = Score()
score_group = pygame.sprite.Group()
score_group.add(score)

high_score = HighScore()
high_score_group = pygame.sprite.Group()
high_score_group.add(high_score)

play_again = PlayAgain()
play_again_group = pygame.sprite.Group()
play_again_group.add(play_again)

play_cpu = PlayCPU()
play_cpu_group = pygame.sprite.Group()
play_cpu_group.add(play_cpu)

one_player = PlayerCount(0)
two_players = PlayerCount(1)
player_count_group = pygame.sprite.Group()
player_count_group.add(one_player, two_players)

snake_speed = SnakeSpeed()
snake_speed_group = pygame.sprite.Group()
snake_speed_group.add(snake_speed)

title = Title()
title_group = pygame.sprite.Group()
title_group.add(title)

win_message = WinMessage()
win_message_group = pygame.sprite.Group()
win_message_group.add(win_message)

blue_wins = Wins(0)
pink_wins = Wins(1)
wins_group = pygame.sprite.Group()
wins_group.add(blue_wins, pink_wins)

map_message = MapMessage()
map_message_group = pygame.sprite.Group()
map_message_group.add(map_message)
