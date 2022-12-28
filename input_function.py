def input_num_x() -> int:
    while True:
        try:
            num = int(input('Xодят крестики: '))
            if 0 < num < 10:
                return num
            else:
                print('ERROR: Нужно ввести число от 1 до 9.')
        except:
            print('ERROR: Нужно ввести целое число!')


def input_num_o() -> int:
    while True:
        try:
            num = int(input('Xодят нолики: '))
            if 0 < num < 10:
                return num
            else:
                print('ERROR: Нужно ввести число от 1 до 9.')
        except:
            print('ERROR: Нужно ввести целое число!')


def rand_or_human() -> bool:
    res = True
    while True:
        res_str = input('Хотите сразиться с богом рандома? (Y/N): ').lower().replace(' ', '')
        if res_str == 'y' or res_str == 'n':
            if res_str == 'y':
                return res
            else:
                res = False
                return res
        else:
            print('Введите только Y или N ')
        
def input_method() -> bool:
    res = True
    while True:
        res_str = input('Вы будете ходить на цифровом блоке клавиатуры? (Y/N): ').lower().replace(' ', '')
        if res_str == 'y' or res_str == 'n':
            if res_str == 'y':
                return res
            else:
                res = False
                return res
        else:
            print('Введите только Y или N ')
