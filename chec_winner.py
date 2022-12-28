def chec_winner(l: list) -> int:
    if ((l[0] == 'x' and l[1] == 'x' and l[2] == 'x')
    or (l[3] == 'x' and l[4] == 'x' and l[5] == 'x')
    or (l[6] == 'x' and l[7] == 'x' and l[8] == 'x')
    or (l[0] == 'x' and l[3] == 'x' and l[6] == 'x')
    or (l[1] == 'x' and l[4] == 'x' and l[7] == 'x')
    or (l[2] == 'x' and l[5] == 'x' and l[8] == 'x')
    or (l[0] == 'x' and l[4] == 'x' and l[8] == 'x')
    or (l[2] == 'x' and l[4] == 'x' and l[6] == 'x')):
        res = 1
        return res

    elif ((l[0] == 'o' and l[1] == 'o' and l[2] == 'o')
    or (l[3] == 'o' and l[4] == 'o' and l[5] == 'o')
    or (l[6] == 'o' and l[7] == 'o' and l[8] == 'o')
    or (l[0] == 'o' and l[3] == 'o' and l[6] == 'o')
    or (l[1] == 'o' and l[4] == 'o' and l[7] == 'o')
    or (l[2] == 'o' and l[5] == 'o' and l[8] == 'o')
    or (l[0] == 'o' and l[4] == 'o' and l[8] == 'o')
    or (l[2] == 'o' and l[4] == 'o' and l[6] == 'o')):
        res = 0
        return res

    else:
        res = 2
        return res



