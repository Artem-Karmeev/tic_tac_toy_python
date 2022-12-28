from input_function import input_num_x
from input_function import input_num_o

def step_х(list_moves: list):
    while True:
        n = input_num_x() - 1
        if list_moves[n] != 'x' and list_moves[n] != 'o':
            list_moves[n] = 'x'
            print(' ')
            break
        else:
            print('ERROR: Место занято')

def step_o(list_moves: list):
    while True:
        n = input_num_o() - 1
        if list_moves[n] != 'x' and list_moves[n] != 'o':
            list_moves[n] = 'o'
            print(' ')
            break
        else:
            print('ERROR: Место занято')