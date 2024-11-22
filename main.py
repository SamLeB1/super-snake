import pygame
from game import game
import bfs
import buttons
import images
import maps
import settings
import text


def render():
    screen.fill("black")
    images.background_group.draw(screen)
    if game.state == "start":
        if text.one_player.is_selected:
            buttons.increment_decrement_group.draw(screen)
            buttons.arrow_group.draw(screen)
            text.play_again_group.draw(screen)
            text.player_count_group.draw(screen)
            text.snake_speed_group.draw(screen)
            maps.maps_group.draw(screen)
            text.title_group.draw(screen)
        elif text.two_players.is_selected:
            buttons.increment_decrement_group.draw(screen)
            buttons.arrow_group.draw(screen)
            text.play_again_group.draw(screen)
            text.player_count_group.draw(screen)
            text.play_cpu_group.draw(screen)
            text.snake_speed_group.draw(screen)
            maps.maps_group.draw(screen)
            text.title_group.draw(screen)

    if game.state == "active":
        for item in maps.maps.current_map:
            screen.blit(spike, (item[0] * 40, item[1] * 40))
        for item in game.snake:
            if item == game.snake[0]:
                if game.snake_direction == "up":
                    screen.blit(snake_head_blue_img[0], (item[0] * 40, item[1] * 40))
                elif game.snake_direction == "down":
                    screen.blit(snake_head_blue_img[1], (item[0] * 40, item[1] * 40))
                elif game.snake_direction == "left":
                    screen.blit(snake_head_blue_img[2], (item[0] * 40, item[1] * 40))
                elif game.snake_direction == "right":
                    screen.blit(snake_head_blue_img[3], (item[0] * 40, item[1] * 40))
            else:
                screen.blit(snake_segment_blue_img, (item[0]*40, item[1]*40))
        screen.blit(apple, (game.apple[0]*40, game.apple[1]*40, 40, 40))
        text.countdown_group.draw(screen)
        text.map_message_group.draw(screen)
        text.score_group.draw(screen)

    elif game.state == "active_2p":
        for item in maps.maps.current_map:
            screen.blit(spike, (item[0] * 40, item[1] * 40))
        for item in game.snake_2p_blue:
            if item == game.snake_2p_blue[0]:
                if game.snake_2p_blue_direction == "up":
                    screen.blit(snake_head_blue_img[0], (item[0] * 40, item[1] * 40))
                elif game.snake_2p_blue_direction == "down":
                    screen.blit(snake_head_blue_img[1], (item[0] * 40, item[1] * 40))
                elif game.snake_2p_blue_direction == "left":
                    screen.blit(snake_head_blue_img[2], (item[0] * 40, item[1] * 40))
                elif game.snake_2p_blue_direction == "right":
                    screen.blit(snake_head_blue_img[3], (item[0] * 40, item[1] * 40))
            else:
                screen.blit(snake_segment_blue_img, (item[0]*40, item[1]*40))
        for item in game.snake_2p_pink:
            if item == game.snake_2p_pink[0]:
                if game.snake_2p_pink_direction == "up":
                    screen.blit(snake_head_pink_img[0], (item[0] * 40, item[1] * 40))
                elif game.snake_2p_pink_direction == "down":
                    screen.blit(snake_head_pink_img[1], (item[0] * 40, item[1] * 40))
                elif game.snake_2p_pink_direction == "left":
                    screen.blit(snake_head_pink_img[2], (item[0] * 40, item[1] * 40))
                elif game.snake_2p_pink_direction == "right":
                    screen.blit(snake_head_pink_img[3], (item[0] * 40, item[1] * 40))
            else:
                screen.blit(snake_segment_pink_img, (item[0]*40, item[1]*40))
        screen.blit(apple, (game.apple[0] * 40, game.apple[1] * 40, 40, 40))
        text.countdown_group.draw(screen)
        text.map_message_group.draw(screen)

    elif game.state == "active_cpu":
        for item in maps.maps.current_map:
            screen.blit(spike, (item[0] * 40, item[1] * 40))
        for item in game.snake_2p_blue:
            if item == game.snake_2p_blue[0]:
                if game.snake_2p_blue_direction == "up":
                    screen.blit(snake_head_blue_img[0], (item[0] * 40, item[1] * 40))
                elif game.snake_2p_blue_direction == "down":
                    screen.blit(snake_head_blue_img[1], (item[0] * 40, item[1] * 40))
                elif game.snake_2p_blue_direction == "left":
                    screen.blit(snake_head_blue_img[2], (item[0] * 40, item[1] * 40))
                elif game.snake_2p_blue_direction == "right":
                    screen.blit(snake_head_blue_img[3], (item[0] * 40, item[1] * 40))
            else:
                screen.blit(snake_segment_blue_img, (item[0]*40, item[1]*40))
        for item in game.snake_2p_pink:
            if item == game.snake_2p_pink[0]:
                if game.cpu_direction == "up":
                    screen.blit(snake_head_pink_img[0], (item[0] * 40, item[1] * 40))
                elif game.cpu_direction == "down":
                    screen.blit(snake_head_pink_img[1], (item[0] * 40, item[1] * 40))
                elif game.cpu_direction == "left":
                    screen.blit(snake_head_pink_img[2], (item[0] * 40, item[1] * 40))
                elif game.cpu_direction == "right":
                    screen.blit(snake_head_pink_img[3], (item[0] * 40, item[1] * 40))
            else:
                screen.blit(snake_segment_pink_img, (item[0]*40, item[1]*40))
        screen.blit(apple, (game.apple[0] * 40, game.apple[1] * 40, 40, 40))
        text.countdown_group.draw(screen)
        text.map_message_group.draw(screen)

    elif game.state == "inactive":
        if text.one_player.is_selected:
            buttons.increment_decrement_group.draw(screen)
            buttons.arrow_group.draw(screen)
            text.high_score_group.draw(screen)
            text.play_again_group.draw(screen)
            text.player_count_group.draw(screen)
            text.score_group.draw(screen)
            text.snake_speed_group.draw(screen)
            maps.maps_group.draw(screen)
        elif text.two_players.is_selected:
            buttons.increment_decrement_group.draw(screen)
            buttons.arrow_group.draw(screen)
            text.play_again_group.draw(screen)
            text.player_count_group.draw(screen)
            text.play_cpu_group.draw(screen)
            text.snake_speed_group.draw(screen)
            maps.maps_group.draw(screen)
            text.win_message_group.draw(screen)
            text.wins_group.draw(screen)
    pygame.display.flip()
    clock.tick(settings.fps)


pygame.init()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
clock = pygame.time.Clock()
running = True
timer = pygame.time.get_ticks()

apple = pygame.image.load("assets/sprites/apple.png")
spike = pygame.image.load("assets/sprites/spike.png")
snake_segment_blue_img = pygame.image.load("assets/sprites/snake_segment_blue.png")
snake_segment_pink_img = pygame.image.load("assets/sprites/snake_segment_pink.png")
snake_head_blue_img = [pygame.image.load("assets/sprites/snake_head_up_blue.png"),
                       pygame.image.load("assets/sprites/snake_head_down_blue.png"),
                       pygame.image.load("assets/sprites/snake_head_left_blue.png"),
                       pygame.image.load("assets/sprites/snake_head_right_blue.png")]
snake_head_pink_img = [pygame.image.load("assets/sprites/snake_head_up_pink.png"),
                       pygame.image.load("assets/sprites/snake_head_down_pink.png"),
                       pygame.image.load("assets/sprites/snake_head_left_pink.png"),
                       pygame.image.load("assets/sprites/snake_head_right_pink.png")]

pygame.display.set_caption("Super Snake")
pygame.display.set_icon(pygame.image.load("assets/sprites/icon.ico"))

pygame.mixer.init()
pygame.mixer.music.load("assets/sounds/bgm_action_4.mp3")
pygame.mixer.music.play(-1)

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    if game.state == "start":
        images.background.update()
        buttons.increment.update(events)
        buttons.decrement.update(events)
        buttons.arrow_left.update(events)
        buttons.arrow_right.update(events)
        text.play_again.update(events)
        text.play_cpu.update(events)
        text.snake_speed.update()
        maps.maps.update()
        text.one_player.update(events)
        text.two_players.update(events)

    if game.state == "active":
        if pygame.time.get_ticks() - text.play_again.static_time >= 3000:
            images.background.reset()
            text.win_message.identifier = 0
            keys = pygame.key.get_pressed()
            if len(game.snake) > 1:
                if keys[pygame.K_w] or keys[pygame.K_UP]:
                    if not game.snake[1][1] == game.snake[0][1] - 1:
                        game.snake_direction = "up"
                if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    if not game.snake[1][1] == game.snake[0][1] + 1:
                        game.snake_direction = "down"
                if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    if not game.snake[1][0] == game.snake[0][0] - 1:
                        game.snake_direction = "left"
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    if not game.snake[1][0] == game.snake[0][0] + 1:
                        game.snake_direction = "right"
            else:
                if keys[pygame.K_w] or keys[pygame.K_UP]:
                    game.snake_direction = "up"
                if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    game.snake_direction = "down"
                if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    game.snake_direction = "left"
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    game.snake_direction = "right"

            if (pygame.time.get_ticks() - timer >= (220 - (text.snake_speed.speed * 20)) +
                    (text.snake_speed.speed * 1.5)):
                game.move_snake()
                timer = pygame.time.get_ticks()

            text.countdown_group.update()
            text.map_message.update()
            text.high_score.update()
            text.play_again.update(events)
            text.score.update()
        else:
            images.background.reset()
            text.win_message.identifier = 0
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                game.snake_direction = "up"
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                game.snake_direction = "down"
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                game.snake_direction = "left"
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                game.snake_direction = "right"

            text.countdown_group.update()
            text.map_message.update()
            text.high_score.update()
            text.play_again.update(events)
            text.score.update()

    elif game.state == "active_2p":
        if pygame.time.get_ticks() - text.play_again.static_time >= 3000:
            images.background.reset()
            keys = pygame.key.get_pressed()
            # Handle blue snake direction
            if len(game.snake_2p_blue) > 1:
                if keys[pygame.K_w]:
                    if not game.snake_2p_blue[1][1] == game.snake_2p_blue[0][1] - 1:
                        game.snake_2p_blue_direction = "up"
                if keys[pygame.K_s]:
                    if not game.snake_2p_blue[1][1] == game.snake_2p_blue[0][1] + 1:
                        game.snake_2p_blue_direction = "down"
                if keys[pygame.K_a]:
                    if not game.snake_2p_blue[1][0] == game.snake_2p_blue[0][0] - 1:
                        game.snake_2p_blue_direction = "left"
                if keys[pygame.K_d]:
                    if not game.snake_2p_blue[1][0] == game.snake_2p_blue[0][0] + 1:
                        game.snake_2p_blue_direction = "right"
            else:
                if keys[pygame.K_w]:
                    game.snake_2p_blue_direction = "up"
                if keys[pygame.K_s]:
                    game.snake_2p_blue_direction = "down"
                if keys[pygame.K_a]:
                    game.snake_2p_blue_direction = "left"
                if keys[pygame.K_d]:
                    game.snake_2p_blue_direction = "right"

            # Handle pink snake direction
            if len(game.snake_2p_pink) > 1:
                if keys[pygame.K_UP]:
                    if not game.snake_2p_pink[1][1] == game.snake_2p_pink[0][1] - 1:
                        game.snake_2p_pink_direction = "up"
                if keys[pygame.K_DOWN]:
                    if not game.snake_2p_pink[1][1] == game.snake_2p_pink[0][1] + 1:
                        game.snake_2p_pink_direction = "down"
                if keys[pygame.K_LEFT]:
                    if not game.snake_2p_pink[1][0] == game.snake_2p_pink[0][0] - 1:
                        game.snake_2p_pink_direction = "left"
                if keys[pygame.K_RIGHT]:
                    if not game.snake_2p_pink[1][0] == game.snake_2p_pink[0][0] + 1:
                        game.snake_2p_pink_direction = "right"
            else:
                if keys[pygame.K_UP]:
                    game.snake_2p_pink_direction = "up"
                if keys[pygame.K_DOWN]:
                    game.snake_2p_pink_direction = "down"
                if keys[pygame.K_LEFT]:
                    game.snake_2p_pink_direction = "left"
                if keys[pygame.K_RIGHT]:
                    game.snake_2p_pink_direction = "right"

            if (pygame.time.get_ticks() - timer >= (220 - (text.snake_speed.speed * 20)) +
                    (text.snake_speed.speed * 1.5)):
                game.move_snake_2p_blue()
                game.move_snake_2p_pink()
                timer = pygame.time.get_ticks()

            text.countdown_group.update()
            text.map_message.update()
            text.play_again.update(events)

        else:
            images.background.reset()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                game.snake_2p_blue_direction = "up"
            if keys[pygame.K_s]:
                game.snake_2p_blue_direction = "down"
            if keys[pygame.K_a]:
                game.snake_2p_blue_direction = "left"
            if keys[pygame.K_d]:
                game.snake_2p_blue_direction = "right"
            if keys[pygame.K_UP]:
                game.snake_2p_pink_direction = "up"
            if keys[pygame.K_DOWN]:
                game.snake_2p_pink_direction = "down"
            if keys[pygame.K_LEFT]:
                game.snake_2p_pink_direction = "left"
            if keys[pygame.K_RIGHT]:
                game.snake_2p_pink_direction = "right"

            text.countdown_group.update()
            text.map_message.update()
            text.play_again.update(events)

    elif game.state == "active_cpu":
        if pygame.time.get_ticks() - text.play_cpu.static_time >= 3000:
            images.background.reset()
            keys = pygame.key.get_pressed()
            # Handle blue snake direction
            if len(game.snake_2p_blue) > 1:
                if keys[pygame.K_w] or keys[pygame.K_UP]:
                    if not game.snake_2p_blue[1][1] == game.snake_2p_blue[0][1] - 1:
                        game.snake_2p_blue_direction = "up"
                if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    if not game.snake_2p_blue[1][1] == game.snake_2p_blue[0][1] + 1:
                        game.snake_2p_blue_direction = "down"
                if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    if not game.snake_2p_blue[1][0] == game.snake_2p_blue[0][0] - 1:
                        game.snake_2p_blue_direction = "left"
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    if not game.snake_2p_blue[1][0] == game.snake_2p_blue[0][0] + 1:
                        game.snake_2p_blue_direction = "right"
            else:
                if keys[pygame.K_w] or keys[pygame.K_UP]:
                    game.snake_2p_blue_direction = "up"
                if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    game.snake_2p_blue_direction = "down"
                if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    game.snake_2p_blue_direction = "left"
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    game.snake_2p_blue_direction = "right"

            if (pygame.time.get_ticks() - timer >= (220 - (text.snake_speed.speed * 20)) +
                    (text.snake_speed.speed * 1.5)):
                # Update game board
                game.board = [[0] * 16 for i in range(16)]
                for i in maps.maps.current_map:
                    game.board[i[1]][i[0]] = 2
                for i in game.snake_2p_pink:
                    game.board[i[1]][i[0]] = 2
                    if i == game.snake_2p_pink[0]:
                        game.board[i[1]][i[0]] = 1
                for i in game.snake_2p_blue:
                    game.board[i[1]][i[0]] = 2
                game.board[game.apple[1]][game.apple[0]] = 3

                text.countdown_group.update()
                text.map_message.update()
                text.play_again.update(events)
                game.move_snake_2p_blue()
                next_move = bfs.get_next_move()
                game.cpu_direction = next_move
                game.move_snake_cpu(next_move)
                timer = pygame.time.get_ticks()
        else:
            images.background.reset()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                game.snake_2p_blue_direction = "up"
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                game.snake_2p_blue_direction = "down"
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                game.snake_2p_blue_direction = "left"
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                game.snake_2p_blue_direction = "right"

            text.countdown_group.update()
            text.map_message.update()
            text.play_again.update(events)

    elif game.state == "set_wins":
        if maps.maps.random_is_selected:
            maps.maps.selected_map_index = 0
            maps.maps.update()
        if game.blue_wins == game.blue_wins_old + 1 and game.pink_wins == game.pink_wins_old + 1:
            text.win_message.identifier = 3
            game.blue_wins -= 1
            game.pink_wins -= 1
        elif game.blue_wins == game.blue_wins_old + 1:
            text.win_message.identifier = 1
        elif game.pink_wins == game.pink_wins_old + 1:
            text.win_message.identifier = 2

        text.blue_wins.update()
        text.pink_wins.update()
        text.win_message.update()
        game.state = "inactive"

    elif game.state == "inactive":
        images.background.update()
        buttons.increment.update(events)
        buttons.decrement.update(events)
        buttons.arrow_left.update(events)
        buttons.arrow_right.update(events)
        text.play_again.update(events)
        text.play_cpu.update(events)
        text.snake_speed.update()
        maps.maps.update()
        text.one_player.update(events)
        text.two_players.update(events)
        text.map_message.offset = -32
        text.map_message.update()

    render()

pygame.quit()
