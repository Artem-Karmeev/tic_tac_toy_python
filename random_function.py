from random import randint

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list2 = ['o', 'o', 'o', 4, 'o', 'o', 'o', 'o', 'o']


def rand_step(list_moves: list):
    while True:
        num = randint(0, 8)
        if list_moves[num] != 'x' or list_moves[num] != 'o':
            list_moves[num] = 'x'
            break

               
print(rand_step(my_list2))



