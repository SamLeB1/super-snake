import pygame
import maps
import copy
import random


class Game:
    def __init__(self):
        self.state = "start"
        self.board = [[0]*16 for _ in range(16)]
        self.apple = []
        pygame.mixer.init()
        self.apple_crunch_sfx = pygame.mixer.Sound("assets/sounds/apple_crunch.mp3")
        self.apple_crunch_sfx.set_volume(0.4)

        self.snake = [[2, 2]]
        self.snake_direction = "right"
        self.snake_2p_blue = [[2, 2]]
        self.snake_2p_blue_direction = "right"
        self.snake_2p_pink = [[13, 13]]
        self.snake_2p_pink_direction = "left"
        self.cpu_direction = "left"

        self.blue_wins = 0
        self.blue_wins_old = 0
        self.pink_wins = 0
        self.pink_wins_old = 0

    def init(self):
        self.snake.clear()
        self.snake.append([2, 2])
        self.snake_direction = "right"

        self.snake_2p_blue.clear()
        self.snake_2p_blue.append([2, 2])
        self.snake_2p_blue_direction = "right"
        self.snake_2p_pink.clear()
        self.snake_2p_pink.append([13, 13])
        self.snake_2p_pink_direction = "left"
        self.cpu_direction = "left"

        if maps.maps.random_is_selected:
            maps.maps.selected_map_index = random.randint(1, 26)
            maps.maps.update()
        self.blue_wins_old = self.blue_wins
        self.pink_wins_old = self.pink_wins
        self.spawn_apple()

    def move_snake(self):
        if self.snake_direction == "up":
            # Check border collision
            if self.snake[0][1] - 1 < 0:
                if maps.maps.random_is_selected:
                    maps.maps.selected_map_index = 0
                    maps.maps.update()
                self.state = "inactive"
                return
            # Check self collision
            elif [self.snake[0][0], self.snake[0][1] - 1] in self.snake:
                if maps.maps.random_is_selected:
                    maps.maps.selected_map_index = 0
                    maps.maps.update()
                self.state = "inactive"
                return
            # Check wall collision
            elif [self.snake[0][0], self.snake[0][1] - 1] in maps.maps.current_map:
                if maps.maps.random_is_selected:
                    maps.maps.selected_map_index = 0
                    maps.maps.update()
                self.state = "inactive"
                return
            # Check apple collision
            elif self.snake[0][0] == self.apple[0] and self.snake[0][1] - 1 == self.apple[1]:
                self.snake.insert(0, [self.apple[0], self.apple[1]])
                self.apple_crunch_sfx.play()
                self.spawn_apple()
                return
            else:
                snake_copy = copy.deepcopy(self.snake)
                self.snake[0][1] -= 1
                for i in range(1, len(snake_copy)):
                    self.snake[i] = snake_copy[i - 1]
        elif self.snake_direction == "down":
            # Check border collision
            if self.snake[0][1] + 1 > 15:
                if maps.maps.random_is_selected:
                    maps.maps.selected_map_index = 0
                    maps.maps.update()
                self.state = "inactive"
                return
            # Check self collision
            elif [self.snake[0][0], self.snake[0][1] + 1] in self.snake:
                if maps.maps.random_is_selected:
                    maps.maps.selected_map_index = 0
                    maps.maps.update()
                self.state = "inactive"
                return
            # Check wall collision
            elif [self.snake[0][0], self.snake[0][1] + 1] in maps.maps.current_map:
                if maps.maps.random_is_selected:
                    maps.maps.selected_map_index = 0
                    maps.maps.update()
                self.state = "inactive"
                return
            # Check apple collision
            elif self.snake[0][0] == self.apple[0] and self.snake[0][1] + 1 == self.apple[1]:
                self.snake.insert(0, [self.apple[0], self.apple[1]])
                self.apple_crunch_sfx.play()
                self.spawn_apple()
                return
            else:
                snake_copy = copy.deepcopy(self.snake)
                self.snake[0][1] += 1
                for i in range(1, len(snake_copy)):
                    self.snake[i] = snake_copy[i - 1]
        elif self.snake_direction == "left":
            # Check border collision
            if self.snake[0][0] - 1 < 0:
                if maps.maps.random_is_selected:
                    maps.maps.selected_map_index = 0
                    maps.maps.update()
                self.state = "inactive"
                return
            # Check self collision
            elif [self.snake[0][0] - 1, self.snake[0][1]] in self.snake:
                if maps.maps.random_is_selected:
                    maps.maps.selected_map_index = 0
                    maps.maps.update()
                self.state = "inactive"
                return
            # Check wall collision
            elif [self.snake[0][0] - 1, self.snake[0][1]] in maps.maps.current_map:
                if maps.maps.random_is_selected:
                    maps.maps.selected_map_index = 0
                    maps.maps.update()
                self.state = "inactive"
                return
            # Check apple collision
            elif self.snake[0][0] - 1 == self.apple[0] and self.snake[0][1] == self.apple[1]:
                self.snake.insert(0, [self.apple[0], self.apple[1]])
                self.apple_crunch_sfx.play()
                self.spawn_apple()
                return
            else:
                snake_copy = copy.deepcopy(self.snake)
                self.snake[0][0] -= 1
                for i in range(1, len(snake_copy)):
                    self.snake[i] = snake_copy[i - 1]
        elif self.snake_direction == "right":
            # Check border collision
            if self.snake[0][0] + 1 > 15:
                if maps.maps.random_is_selected:
                    maps.maps.selected_map_index = 0
                    maps.maps.update()
                self.state = "inactive"
                return
            # Check self collision
            elif [self.snake[0][0] + 1, self.snake[0][1]] in self.snake:
                if maps.maps.random_is_selected:
                    maps.maps.selected_map_index = 0
                    maps.maps.update()
                self.state = "inactive"
                return
            # Check wall collision
            elif [self.snake[0][0] + 1, self.snake[0][1]] in maps.maps.current_map:
                if maps.maps.random_is_selected:
                    maps.maps.selected_map_index = 0
                    maps.maps.update()
                self.state = "inactive"
                return
            # Check apple collision
            elif self.snake[0][0] + 1 == self.apple[0] and self.snake[0][1] == self.apple[1]:
                self.snake.insert(0, [self.apple[0], self.apple[1]])
                self.apple_crunch_sfx.play()
                self.spawn_apple()
                return
            else:
                snake_copy = copy.deepcopy(self.snake)
                self.snake[0][0] += 1
                for i in range(1, len(snake_copy)):
                    self.snake[i] = snake_copy[i - 1]

    def move_snake_2p_blue(self):
        if self.snake_2p_blue_direction == "up":
            # Check border collision
            if self.snake_2p_blue[0][1] - 1 < 0:
                self.state = "set_wins"
                self.pink_wins += 1
                return
            # Check self collision
            elif [self.snake_2p_blue[0][0], self.snake_2p_blue[0][1] - 1] in self.snake_2p_blue:
                self.state = "set_wins"
                self.pink_wins += 1
                return
            # Check wall collision
            elif [self.snake_2p_blue[0][0], self.snake_2p_blue[0][1] - 1] in maps.maps.current_map:
                self.state = "set_wins"
                self.pink_wins += 1
                return
            # Check other player collision
            elif [self.snake_2p_blue[0][0], self.snake_2p_blue[0][1] - 1] in self.snake_2p_pink:
                self.state = "set_wins"
                self.pink_wins += 1
                return
            # Check apple collision
            elif self.snake_2p_blue[0][0] == self.apple[0] and self.snake_2p_blue[0][1] - 1 == self.apple[1]:
                self.snake_2p_blue.insert(0, [self.apple[0], self.apple[1]])
                self.apple_crunch_sfx.play()
                self.spawn_apple()
                return
            else:
                snake_copy = copy.deepcopy(self.snake_2p_blue)
                self.snake_2p_blue[0][1] -= 1
                for i in range(1, len(snake_copy)):
                    self.snake_2p_blue[i] = snake_copy[i - 1]
        elif self.snake_2p_blue_direction == "down":
            # Check border collision
            if self.snake_2p_blue[0][1] + 1 > 15:
                self.state = "set_wins"
                self.pink_wins += 1
                return
            # Check self collision
            elif [self.snake_2p_blue[0][0], self.snake_2p_blue[0][1] + 1] in self.snake_2p_blue:
                self.state = "set_wins"
                self.pink_wins += 1
                return
            # Check wall collision
            elif [self.snake_2p_blue[0][0], self.snake_2p_blue[0][1] + 1] in maps.maps.current_map:
                self.state = "set_wins"
                self.pink_wins += 1
                return
            # Check other player collision
            elif [self.snake_2p_blue[0][0], self.snake_2p_blue[0][1] + 1] in self.snake_2p_pink:
                self.state = "set_wins"
                self.pink_wins += 1
                return
            # Check apple collision
            elif self.snake_2p_blue[0][0] == self.apple[0] and self.snake_2p_blue[0][1] + 1 == self.apple[1]:
                self.snake_2p_blue.insert(0, [self.apple[0], self.apple[1]])
                self.apple_crunch_sfx.play()
                self.spawn_apple()
                return
            else:
                snake_copy = copy.deepcopy(self.snake_2p_blue)
                self.snake_2p_blue[0][1] += 1
                for i in range(1, len(snake_copy)):
                    self.snake_2p_blue[i] = snake_copy[i - 1]
        elif self.snake_2p_blue_direction == "left":
            # Check border collision
            if self.snake_2p_blue[0][0] - 1 < 0:
                self.state = "set_wins"
                self.pink_wins += 1
                return
            # Check self collision
            elif [self.snake_2p_blue[0][0] - 1, self.snake_2p_blue[0][1]] in self.snake_2p_blue:
                self.state = "set_wins"
                self.pink_wins += 1
                return
            # Check wall collision
            elif [self.snake_2p_blue[0][0] - 1, self.snake_2p_blue[0][1]] in maps.maps.current_map:
                self.state = "set_wins"
                self.pink_wins += 1
                return
            # Check other player collision
            elif [self.snake_2p_blue[0][0] - 1, self.snake_2p_blue[0][1]] in self.snake_2p_pink:
                self.state = "set_wins"
                self.pink_wins += 1
                return
            # Check apple collision
            elif self.snake_2p_blue[0][0] - 1 == self.apple[0] and self.snake_2p_blue[0][1] == self.apple[1]:
                self.snake_2p_blue.insert(0, [self.apple[0], self.apple[1]])
                self.apple_crunch_sfx.play()
                self.spawn_apple()
                return
            else:
                snake_copy = copy.deepcopy(self.snake_2p_blue)
                self.snake_2p_blue[0][0] -= 1
                for i in range(1, len(snake_copy)):
                    self.snake_2p_blue[i] = snake_copy[i - 1]
        elif self.snake_2p_blue_direction == "right":
            # Check border collision
            if self.snake_2p_blue[0][0] + 1 > 15:
                self.state = "set_wins"
                self.pink_wins += 1
                return
            # Check self collision
            elif [self.snake_2p_blue[0][0] + 1, self.snake_2p_blue[0][1]] in self.snake_2p_blue:
                self.state = "set_wins"
                self.pink_wins += 1
                return
            # Check wall collision
            elif [self.snake_2p_blue[0][0] + 1, self.snake_2p_blue[0][1]] in maps.maps.current_map:
                self.state = "set_wins"
                self.pink_wins += 1
                return
            # Check other player collision
            elif [self.snake_2p_blue[0][0] + 1, self.snake_2p_blue[0][1]] in self.snake_2p_pink:
                self.state = "set_wins"
                self.pink_wins += 1
                return
            # Check apple collision
            elif self.snake_2p_blue[0][0] + 1 == self.apple[0] and self.snake_2p_blue[0][1] == self.apple[1]:
                self.snake_2p_blue.insert(0, [self.apple[0], self.apple[1]])
                self.apple_crunch_sfx.play()
                self.spawn_apple()
                return
            else:
                snake_copy = copy.deepcopy(self.snake_2p_blue)
                self.snake_2p_blue[0][0] += 1
                for i in range(1, len(snake_copy)):
                    self.snake_2p_blue[i] = snake_copy[i - 1]

    def move_snake_2p_pink(self):
        if self.snake_2p_pink_direction == "up":
            # Check border collision
            if self.snake_2p_pink[0][1] - 1 < 0:
                self.state = "set_wins"
                self.blue_wins += 1
                return
            # Check self collision
            elif [self.snake_2p_pink[0][0], self.snake_2p_pink[0][1] - 1] in self.snake_2p_pink:
                self.state = "set_wins"
                self.blue_wins += 1
                return
            # Check wall collision
            elif [self.snake_2p_pink[0][0], self.snake_2p_pink[0][1] - 1] in maps.maps.current_map:
                self.state = "set_wins"
                self.blue_wins += 1
                return
            # Check other player collision
            elif [self.snake_2p_pink[0][0], self.snake_2p_pink[0][1] - 1] in self.snake_2p_blue:
                self.state = "set_wins"
                self.blue_wins += 1
                if [self.snake_2p_pink[0][0], self.snake_2p_pink[0][1] - 1] == self.snake_2p_blue[0]:
                    self.pink_wins += 1
                return
            # Check apple collision
            elif self.snake_2p_pink[0][0] == self.apple[0] and self.snake_2p_pink[0][1] - 1 == self.apple[1]:
                self.snake_2p_pink.insert(0, [self.apple[0], self.apple[1]])
                self.apple_crunch_sfx.play()
                self.spawn_apple()
                return
            else:
                snake_copy = copy.deepcopy(self.snake_2p_pink)
                self.snake_2p_pink[0][1] -= 1
                for i in range(1, len(snake_copy)):
                    self.snake_2p_pink[i] = snake_copy[i - 1]
        elif self.snake_2p_pink_direction == "down":
            # Check border collision
            if self.snake_2p_pink[0][1] + 1 > 15:
                self.state = "set_wins"
                self.blue_wins += 1
                return
            # Check self collision
            elif [self.snake_2p_pink[0][0], self.snake_2p_pink[0][1] + 1] in self.snake_2p_pink:
                self.state = "set_wins"
                self.blue_wins += 1
                return
            # Check wall collision
            elif [self.snake_2p_pink[0][0], self.snake_2p_pink[0][1] + 1] in maps.maps.current_map:
                self.state = "set_wins"
                self.blue_wins += 1
                return
            # Check other player collision
            elif [self.snake_2p_pink[0][0], self.snake_2p_pink[0][1] + 1] in self.snake_2p_blue:
                self.state = "set_wins"
                self.blue_wins += 1
                if [self.snake_2p_pink[0][0], self.snake_2p_pink[0][1] + 1] == self.snake_2p_blue[0]:
                    self.pink_wins += 1
                return
            # Check apple collision
            elif self.snake_2p_pink[0][0] == self.apple[0] and self.snake_2p_pink[0][1] + 1 == self.apple[1]:
                self.snake_2p_pink.insert(0, [self.apple[0], self.apple[1]])
                self.apple_crunch_sfx.play()
                self.spawn_apple()
                return
            else:
                snake_copy = copy.deepcopy(self.snake_2p_pink)
                self.snake_2p_pink[0][1] += 1
                for i in range(1, len(snake_copy)):
                    self.snake_2p_pink[i] = snake_copy[i - 1]
        elif self.snake_2p_pink_direction == "left":
            # Check border collision
            if self.snake_2p_pink[0][0] - 1 < 0:
                self.state = "set_wins"
                self.blue_wins += 1
                return
            # Check self collision
            elif [self.snake_2p_pink[0][0] - 1, self.snake_2p_pink[0][1]] in self.snake_2p_pink:
                self.state = "set_wins"
                self.blue_wins += 1
                return
            # Check wall collision
            elif [self.snake_2p_pink[0][0] - 1, self.snake_2p_pink[0][1]] in maps.maps.current_map:
                self.state = "set_wins"
                self.blue_wins += 1
                return
            # Check other player collision
            elif [self.snake_2p_pink[0][0] - 1, self.snake_2p_pink[0][1]] in self.snake_2p_blue:
                self.state = "set_wins"
                self.blue_wins += 1
                if [self.snake_2p_pink[0][0] - 1, self.snake_2p_pink[0][1]] == self.snake_2p_blue[0]:
                    self.pink_wins += 1
                return
            # Check apple collision
            elif self.snake_2p_pink[0][0] - 1 == self.apple[0] and self.snake_2p_pink[0][1] == self.apple[1]:
                self.snake_2p_pink.insert(0, [self.apple[0], self.apple[1]])
                self.apple_crunch_sfx.play()
                self.spawn_apple()
                return
            else:
                snake_copy = copy.deepcopy(self.snake_2p_pink)
                self.snake_2p_pink[0][0] -= 1
                for i in range(1, len(snake_copy)):
                    self.snake_2p_pink[i] = snake_copy[i - 1]
        elif self.snake_2p_pink_direction == "right":
            # Check border collision
            if self.snake_2p_pink[0][0] + 1 > 15:
                self.state = "set_wins"
                self.blue_wins += 1
                return
            # Check self collision
            elif [self.snake_2p_pink[0][0] + 1, self.snake_2p_pink[0][1]] in self.snake_2p_pink:
                self.state = "set_wins"
                self.blue_wins += 1
                return
            # Check wall collision
            elif [self.snake_2p_pink[0][0] + 1, self.snake_2p_pink[0][1]] in maps.maps.current_map:
                self.state = "set_wins"
                self.blue_wins += 1
                return
            # Check other player collision
            elif [self.snake_2p_pink[0][0] + 1, self.snake_2p_pink[0][1]] in self.snake_2p_blue:
                self.state = "set_wins"
                self.blue_wins += 1
                if [self.snake_2p_pink[0][0] + 1, self.snake_2p_pink[0][1]] == self.snake_2p_blue[0]:
                    self.pink_wins += 1
                return
            # Check apple collision
            elif self.snake_2p_pink[0][0] + 1 == self.apple[0] and self.snake_2p_pink[0][1] == self.apple[1]:
                self.snake_2p_pink.insert(0, [self.apple[0], self.apple[1]])
                self.apple_crunch_sfx.play()
                self.spawn_apple()
                return
            else:
                snake_copy = copy.deepcopy(self.snake_2p_pink)
                self.snake_2p_pink[0][0] += 1
                for i in range(1, len(snake_copy)):
                    self.snake_2p_pink[i] = snake_copy[i - 1]

    def move_snake_cpu(self, next_move):
        if (not self.cpu_can_move_up() and not self.cpu_can_move_down()
                and not self.cpu_can_move_left() and not self.cpu_can_move_right()):
            if ([self.snake_2p_pink[0][0], self.snake_2p_pink[0][1] - 1] == self.snake_2p_blue[0]
                    or [self.snake_2p_pink[0][0], self.snake_2p_pink[0][1] + 1] == self.snake_2p_blue[0]
                    or [self.snake_2p_pink[0][0] - 1, self.snake_2p_pink[0][1]] == self.snake_2p_blue[0]
                    or [self.snake_2p_pink[0][0] + 1, self.snake_2p_pink[0][1]] == self.snake_2p_blue[0]):
                self.pink_wins += 1
            self.state = "set_wins"
            self.blue_wins += 1
            return
        # Move up
        if next_move == "up":
            # Check apple collision
            if self.snake_2p_pink[0][0] == self.apple[0] and self.snake_2p_pink[0][1] - 1 == self.apple[1]:
                self.snake_2p_pink.insert(0, [self.apple[0], self.apple[1]])
                self.apple_crunch_sfx.play()
                self.spawn_apple()
                return
            elif self.cpu_can_move_up():
                self.move_snake_cpu_up()
            else:
                self.move_snake_cpu_random()
        # Move down
        elif next_move == "down":
            # Check apple collision
            if self.snake_2p_pink[0][0] == self.apple[0] and self.snake_2p_pink[0][1] + 1 == self.apple[1]:
                self.snake_2p_pink.insert(0, [self.apple[0], self.apple[1]])
                self.apple_crunch_sfx.play()
                self.spawn_apple()
                return
            elif self.cpu_can_move_down():
                self.move_snake_cpu_down()
            else:
                self.move_snake_cpu_random()
        # Move left
        elif next_move == "left":
            # Check apple collision
            if self.snake_2p_pink[0][0] - 1 == self.apple[0] and self.snake_2p_pink[0][1] == self.apple[1]:
                self.snake_2p_pink.insert(0, [self.apple[0], self.apple[1]])
                self.apple_crunch_sfx.play()
                self.spawn_apple()
                return
            elif self.cpu_can_move_left():
                self.move_snake_cpu_left()
            else:
                self.move_snake_cpu_random()
        # Move right
        elif next_move == "right":
            # Check apple collision
            if self.snake_2p_pink[0][0] + 1 == self.apple[0] and self.snake_2p_pink[0][1] == self.apple[1]:
                self.snake_2p_pink.insert(0, [self.apple[0], self.apple[1]])
                self.apple_crunch_sfx.play()
                self.spawn_apple()
                return
            elif self.cpu_can_move_right():
                self.move_snake_cpu_right()
            else:
                self.move_snake_cpu_random()
        else:
            self.move_snake_cpu_random()

    def move_snake_cpu_up(self):
        self.cpu_direction = "up"
        snake_copy = copy.deepcopy(self.snake_2p_pink)
        self.snake_2p_pink[0][1] -= 1
        for i in range(1, len(snake_copy)):
            self.snake_2p_pink[i] = snake_copy[i - 1]

    def move_snake_cpu_down(self):
        self.cpu_direction = "down"
        snake_copy = copy.deepcopy(self.snake_2p_pink)
        self.snake_2p_pink[0][1] += 1
        for i in range(1, len(snake_copy)):
            self.snake_2p_pink[i] = snake_copy[i - 1]

    def move_snake_cpu_left(self):
        self.cpu_direction = "left"
        snake_copy = copy.deepcopy(self.snake_2p_pink)
        self.snake_2p_pink[0][0] -= 1
        for i in range(1, len(snake_copy)):
            self.snake_2p_pink[i] = snake_copy[i - 1]

    def move_snake_cpu_right(self):
        self.cpu_direction = "right"
        snake_copy = copy.deepcopy(self.snake_2p_pink)
        self.snake_2p_pink[0][0] += 1
        for i in range(1, len(snake_copy)):
            self.snake_2p_pink[i] = snake_copy[i - 1]

    def move_snake_cpu_random(self):
        is_moved = False
        while not is_moved:
            rand = random.randint(0, 3)
            if rand == 0:
                if self.cpu_can_move_up():
                    self.move_snake_cpu_up()
                    is_moved = True
            elif rand == 1:
                if self.cpu_can_move_down():
                    self.move_snake_cpu_down()
                    is_moved = True
            elif rand == 2:
                if self.cpu_can_move_left():
                    self.move_snake_cpu_left()
                    is_moved = True
            elif rand == 3:
                if self.cpu_can_move_right():
                    self.move_snake_cpu_right()
                    is_moved = True

    def cpu_can_move_up(self):
        if ([self.snake_2p_pink[0][0], self.snake_2p_pink[0][1] - 1] in self.snake_2p_pink
                or [self.snake_2p_pink[0][0], self.snake_2p_pink[0][1] - 1] in self.snake_2p_blue
                or [self.snake_2p_pink[0][0], self.snake_2p_pink[0][1] - 1] in maps.maps.current_map
                or self.snake_2p_pink[0][1] - 1 < 0):
            return False
        else:
            return True

    def cpu_can_move_down(self):
        if ([self.snake_2p_pink[0][0], self.snake_2p_pink[0][1] + 1] in self.snake_2p_pink
                or [self.snake_2p_pink[0][0], self.snake_2p_pink[0][1] + 1] in self.snake_2p_blue
                or [self.snake_2p_pink[0][0], self.snake_2p_pink[0][1] + 1] in maps.maps.current_map
                or self.snake_2p_pink[0][1] + 1 > 15):
            return False
        else:
            return True

    def cpu_can_move_left(self):
        if ([self.snake_2p_pink[0][0] - 1, self.snake_2p_pink[0][1]] in self.snake_2p_pink
                or [self.snake_2p_pink[0][0] - 1, self.snake_2p_pink[0][1]] in self.snake_2p_blue
                or [self.snake_2p_pink[0][0] - 1, self.snake_2p_pink[0][1]] in maps.maps.current_map
                or self.snake_2p_pink[0][0] - 1 < 0):
            return False
        else:
            return True

    def cpu_can_move_right(self):
        if ([self.snake_2p_pink[0][0] + 1, self.snake_2p_pink[0][1]] in self.snake_2p_pink
                or [self.snake_2p_pink[0][0] + 1, self.snake_2p_pink[0][1]] in self.snake_2p_blue
                or [self.snake_2p_pink[0][0] + 1, self.snake_2p_pink[0][1]] in maps.maps.current_map
                or self.snake_2p_pink[0][0] + 1 > 15):
            return False
        else:
            return True

    def spawn_apple(self):
        if self.state == "active":
            self.apple = []
            self.apple = [random.randint(0, 15), random.randint(0, 15)]
            if self.apple in self.snake or self.apple in maps.maps.current_map:
                while self.apple in self.snake or self.apple in maps.maps.current_map:
                    self.apple = [random.randint(0, 15), random.randint(0, 15)]
        elif self.state == "active_2p" or "active_cpu":
            self.apple = []
            self.apple = [random.randint(0, 15), random.randint(0, 15)]
            if (self.apple in self.snake_2p_blue or self.apple in self.snake_2p_pink
                    or self.apple in maps.maps.current_map):
                while (self.apple in self.snake_2p_blue or self.apple in self.snake_2p_pink
                       or self.apple in maps.maps.current_map):
                    self.apple = [random.randint(0, 15), random.randint(0, 15)]


game = Game()
