from input_function import rand_or_human
from step_function import step_х
from step_function import step_o
from random_function import rand_step_x
from random_function import rand_step_o
from print_function import print_list
from chec_winner import chec_winner
from random import randint

def play():
    res_list = [1,2,3,4,5,6,7,8,9]

    r_h = rand_or_human()
    draw = randint(0, 1)
    if r_h == True:
        if draw == True:
            print('\nВы играете крестиками. \n')
            print_list(res_list)
            for i in range(5):
                if i != 4:
                    print(' ')
                    step_х(res_list)
                    print_list(res_list)
                    res = chec_winner(res_list)
                    if res == 1:
                        print('Победили х.')
                        break
                    elif res == 0:
                        print('Победили 0.')
                        break
                    print('\nХод ноликов: \n')
                    rand_step_o(res_list)
                    print_list(res_list)
                    res = chec_winner(res_list)
                    if res == 1:
                        print('Победили х.')
                        break
                    elif res == 0:
                        print('Победили 0.')
                        break
                else:
                    print('\nХод ноликов: \n')
                    rand_step_o(res_list)
                    print_list(res_list)
                    print(' ')
                    res = chec_winner(res_list)
                    if res == 1:
                        print('Победили х.')
                    elif res == 0:
                        print('Победили 0.')
                    elif res == 2:
                        print('Похоже у нас ничья')
        else:
            print('\nВы играете ноликами. \n')
            for i in range(5):
                if i != 4:
                    print('\nХод крестиков: \n')
                    rand_step_x(res_list)
                    print_list(res_list)
                    res = chec_winner(res_list)
                    if res == 1:
                        print('Победили х.')
                        break
                    elif res == 0:
                        print('Победили 0.')
                        break
                    print(' ')
                    step_o(res_list)
                    print_list(res_list)
                    res = chec_winner(res_list)
                    if res == 1:
                        print('Победили х.')
                        break
                    elif res == 0:
                        print('Победили 0.')
                        break
                else:
                    print('\nХод ноликов: \n')
                    step_o(res_list)
                    print_list(res_list)
                    print(' ')
                    res = chec_winner(res_list)
                    if res == 1:
                        print('Победили х.')
                    elif res == 0:
                        print('Победили 0.')
                    elif res == 2:
                        print('Похоже у нас ничья')
    else:
            print('')
            print_list(res_list)
            for i in range(5):
                if i != 4:
                    print(' ')
                    step_х(res_list)
                    print_list(res_list)
                    res = chec_winner(res_list)
                    if res == 1:
                        print('Победили х.')
                        break
                    elif res == 0:
                        print('Победили 0.')
                        break
                    print(' ')
                    step_o(res_list) 
                    print_list(res_list)
                    res = chec_winner(res_list)
                    if res == 1:
                        print('Победили х.')
                        break
                    elif res == 0:
                        print('Победили 0.')
                        break
                else:
                    step_o(res_list)
                    print_list(res_list)
                    print(' ')
                    res = chec_winner(res_list)
                    if res == 1:
                        print('Победили х.')
                    elif res == 0:
                        print('Победили 0.')
                    elif res == 2:
                        print('Похоже у нас ничья')

play()