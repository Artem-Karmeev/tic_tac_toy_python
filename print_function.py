my_list = [7, 8, 9, 4, 5, 6, 1, 2, 3]

def print_list(l: list):
    print(f' {l[0]} │ {l[1]} │ {l[2]} ')
    print('───┼───┼───')
    print(f' {l[3]} │ {l[4]} │ {l[5]}')
    print('───┼───┼───')
    print(f' {l[6]} │ {l[7]} │ {l[8]}')

print(print_list(my_list))