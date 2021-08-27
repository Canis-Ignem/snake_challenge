def meassure_distance(l1,l2):
    l = [ l1[i] - l2[i] for i in range(len(l1)) ]
    return abs(sum(l))

def valid_positions(snake):

    checked = []

    for i in range( len(snake) -1):
        if meassure_distance(snake[i], snake[i+1]) != 1 or snake[i] in checked:
            checked.append(snake[i])
            return False
    if snake[-1] in checked:
        return False
    else:
        return True

def allowed_values(board_shape, snake):

    for i in range(len(snake)):
        for j in range(len(snake[i])):
            if snake[i][j] >= board_shape[j] or snake[i][j] < 0:
                return False

    return True

def valid_snake(board_shape, snake):

    assert 1 < len(snake) < 8, "Snake must have more than 1 element and less 8"
    assert 0 < board_shape[0] < 11 and 0 <board_shape[1] < 11, "Boards must have positive size"
    assert len(snake[0]) == 2, "Only two dimmensional coordinates are accepted"
    assert len(board_shape) == 2, "Only two dimmensional boards are accepted"
    assert type(snake) == list or type(snake) == tuple, "The snake must me of type list or tuple"
    assert type(snake[0]) == list or type(snake[0]) == tuple, "Positions must be of type list or tuple"
    assert type(board_shape) == list or type(board_shape) == tuple, "The board shape must be of type list or tuple"
    assert type(board_shape[0]) == int, "The board shape must be of type int"
    assert type(board_shape[1]) == int, "The board shape must be of type int"
    assert type(snake[0][0]) == int, "The snake coordinates must be of type int"
    assert type(snake[0][1]) == int, "The snake coordinates must be of type int"

    return allowed_values(board_shape, snake) and valid_positions(snake)

def valid_move(move, board_shape, snake):

    if move == 'U':
        new_pos = [snake[0][0] - 1, snake[0][1]]
        if new_pos in snake[:-1] or new_pos[0] < 0:
            return False
        else:
            return True

    elif move == 'D':
        new_pos = [snake[0][0] + 1, snake[0][1]]
        if new_pos in snake[:-1] or new_pos[0] >= board_shape[0]:
            return False
        else:
            return True

    elif move == 'L':
        new_pos = [snake[0][0], snake[0][1] - 1]
        if new_pos in snake[:-1] or new_pos[1] < 0:
            return False
        else:
            return True

    elif move == 'R':
        new_pos = [snake[0][0], snake[0][1] + 1]
        if new_pos in snake[:-1]  or new_pos[1] >= board_shape[1]:
            return False
        else:
            return True

    else:
        print("Move not supported")
        return False

def move_snake(snake, move):

    if move.upper() == 'U':
        new_pos = [snake[0][0] - 1, snake[0][1]]
        snake.insert(0, new_pos)
        snake.pop(-1)
        return snake

    elif move == 'D':
        new_pos = [snake[0][0] + 1, snake[0][1]]
        snake.insert(0, new_pos)
        snake.pop(-1)
        return snake

    elif move == 'L':
        new_pos = [snake[0][0], snake[0][1] - 1]
        snake.insert(0, new_pos)
        snake.pop(-1)
        return snake

    elif move == 'R':
        new_pos = [snake[0][0], snake[0][1] + 1]
        snake.insert(0, new_pos)
        snake.pop(-1)
        return snake

    else:
        print("Move not supported")

def numberOfAvailableDifferentPaths(board_shape, snake, depth, max_lenght, path=""):

    assert 0 < max_lenght <21, "The max lenght must be greater than 0 and lesser than 21"

    if valid_snake(board_shape, snake):
        #print( "Depth: ", depth, " Path: ", path, snake)
        for move in MOVES:
            if valid_move(move, board_shape, snake) and depth < max_lenght:
                new_snake = move_snake(snake.copy(), move)
                numberOfAvailableDifferentPaths(board_shape, new_snake, depth + 1, max_lenght, path + move)
            elif depth == max_lenght:
                PATHS.append(path)

def filter(l):

    filtered_list = []
    for i in l:
        if i not in filtered_list and len(i) < 21:
            filtered_list.append(i)
    return filtered_list

MOVES = ["U", "D", "L", "R"]

## TEST Nº1
print(  "TEST Nº1:\n")
PATHS = []
snake1 = [[2, 2], [2, 3], [1, 3], [0, 3], [0, 2], [0, 1], [0, 0]]
board_shape1 = [3, 4]
pos = valid_positions(snake1)
val = valid_snake(board_shape1, snake1)
numberOfAvailableDifferentPaths(board_shape1, snake1, 0, 3)
print("Number of unique paths found: ",len(filter(PATHS)))
print("Paths: ", PATHS)
assert len(filter(PATHS)) == 7, "There are 7 unique paths of length 3"

## TEST Nº2
print(  "TEST Nº2:\n")
PATHS = []
snake2 = [[2,0], [1,0], [0,0], [0,1], [1,1], [2,1]]
board_shape2 = [3, 2]
pos = valid_positions(snake2)
val = valid_snake(board_shape2, snake2)
numberOfAvailableDifferentPaths(board_shape2, snake2, 0, 10)
print("Number of unique paths found: ",len(filter(PATHS)))
print("Paths: ", PATHS)
assert len(filter(PATHS)) == 1, "There is 1 unique path of length 10"


## TEST Nº3

print(  "TEST Nº3:\n") 
PATHS = []
snake3 = [[5,5], [4,5], [4,4], [5,4]]
board_shape3 = [10, 10]
pos = valid_positions(snake3)
val = valid_snake(board_shape3, snake3)
numberOfAvailableDifferentPaths(board_shape3, snake3, 0, 4) 
print("Number of unique paths found: ",len(filter(PATHS)))
print("Paths: ", PATHS)
assert len(filter(PATHS)) == 81, "There are 81 unique paths of length 4"


