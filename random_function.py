from random import randint

def rand_step_x(list_moves: list):
    while True:
        num = randint(0, 8)
        if list_moves[num] == 'x' or list_moves[num] == 'o':
            num = randint(0, 8)
        else:
            list_moves[num] = 'x'
            break

def rand_step_o(list_moves: list):
    while True:
        num = randint(0, 8)
        if list_moves[num] == 'x' or list_moves[num] == 'o':
            num = randint(0, 8)
        else:
            list_moves[num] = 'o'
            break