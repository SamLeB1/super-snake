from game import game
import copy


def search_up(start):
    spaces = 0
    coordinates = copy.deepcopy(start)
    while True:
        if coordinates[0] - 1 < 0:
            return spaces
        elif game.board[coordinates[0] - 1][coordinates[1]] == 2:
            return spaces
        else:
            coordinates[0] -= 1
            spaces += 1


def search_down(start):
    spaces = 0
    coordinates = copy.deepcopy(start)
    while True:
        if coordinates[0] + 1 > 15:
            return spaces
        elif game.board[coordinates[0] + 1][coordinates[1]] == 2:
            return spaces
        else:
            coordinates[0] += 1
            spaces += 1


def search_left(start):
    spaces = 0
    coordinates = copy.deepcopy(start)
    while True:
        if coordinates[1] - 1 < 0:
            return spaces
        elif game.board[coordinates[0]][coordinates[1] - 1] == 2:
            return spaces
        else:
            coordinates[1] -= 1
            spaces += 1


def search_right(start):
    spaces = 0
    coordinates = copy.deepcopy(start)
    while True:
        if coordinates[1] + 1 > 15:
            return spaces
        elif game.board[coordinates[0]][coordinates[1] + 1] == 2:
            return spaces
        else:
            coordinates[1] += 1
            spaces += 1


def find_biggest(spaces_list):
    biggest = spaces_list[0]
    for item in spaces_list:
        if item[1] > biggest[1]:
            biggest = item
    return biggest[0]


def find_furthest_wall_direction(start):
    spaces = [["up", search_up(start)], ["down", search_down(start)], ["left", search_left(start)],
              ["right", search_right(start)]]
    return find_biggest(spaces)
