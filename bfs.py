from game import game
import trapped


def is_int(char):
    try:
        char = int(char)
        char += 1
        return True
    except ValueError:
        return False


def string_to_tuple(string):
    # Get first value
    if is_int(string[2]):
        value_one = int(string[1:3])
    else:
        value_one = int(string[1])
    # Get second value
    if is_int(string[2]):
        if is_int(string[6]):
            value_two = int(string[5:7])
        else:
            value_two = int(string[5])
    else:
        if is_int(string[5]):
            value_two = int(string[4:6])
        else:
            value_two = int(string[4])
    return [value_one, value_two]


def can_move_up(coordinates):
    if coordinates[0] - 1 < 0:
        return False
    elif game.board[coordinates[0] - 1][coordinates[1]] == 2:
        return False
    else:
        return True


def can_move_down(coordinates):
    if coordinates[0] + 1 > 15:
        return False
    elif game.board[coordinates[0] + 1][coordinates[1]] == 2:
        return False
    else:
        return True


def can_move_left(coordinates):
    if coordinates[1] - 1 < 0:
        return False
    elif game.board[coordinates[0]][coordinates[1] - 1] == 2:
        return False
    else:
        return True


def can_move_right(coordinates):
    if coordinates[1] + 1 > 15:
        return False
    elif game.board[coordinates[0]][coordinates[1] + 1] == 2:
        return False
    else:
        return True


def get_next_move():
    start = None
    end = None
    for i in range(16):
        for j in range(16):
            if game.board[i][j] == 1:
                start = [i, j]
            if game.board[i][j] == 3:
                end = [i, j]

    search_list = [start]
    search_dict = {}

    for item in search_list:
        if can_move_up(item):
            if [item[0] - 1, item[1]] not in search_list:
                search_list.append([item[0] - 1, item[1]])
                search_dict[str([item[0] - 1, item[1]])] = str(item)
        if can_move_down(item):
            if [item[0] + 1, item[1]] not in search_list:
                search_list.append([item[0] + 1, item[1]])
                search_dict[str([item[0] + 1, item[1]])] = str(item)
        if can_move_left(item):
            if [item[0], item[1] - 1] not in search_list:
                search_list.append([item[0], item[1] - 1])
                search_dict[str([item[0], item[1] - 1])] = str(item)
        if can_move_right(item):
            if [item[0], item[1] + 1] not in search_list:
                search_list.append([item[0], item[1] + 1])
                search_dict[str([item[0], item[1] + 1])] = str(item)
        if str(end) in search_dict:
            break

    search = str(end)
    shortest_path = [search]
    count = 0
    while search != str(start):
        search = search_dict.get(search)
        shortest_path.insert(0, search)
        if count > 256:
            return trapped.find_furthest_wall_direction(start)
        count += 1

    current_position = string_to_tuple(shortest_path[0])
    next_position = string_to_tuple(shortest_path[1])

    if next_position[0] == current_position[0] - 1:
        return "up"
    elif next_position[0] == current_position[0] + 1:
        return "down"
    elif next_position[1] == current_position[1] - 1:
        return "left"
    elif next_position[1] == current_position[1] + 1:
        return "right"
