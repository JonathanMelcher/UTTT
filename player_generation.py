def Player1(B, t, won):
    if t == 9:
        for i in range(9):
            if won[i] == 0 and any((True for x in B[i] if x == 0)) == True:
                a = i
                break
    else:
        a = t
    b = B[a].index(0)
    return a,b

import numpy.random as rng


def Player2(B,t, won):
    if t == 9:
        list = []
        for i in range(9):
            if won[i] == 0 and any((True for x in B[i] if x == 0)) == True:
                list.append(i)
        a = rng.choice(list)
    else:
        a = t
    list =[]
    for i in range(9):
        if B[a][i] == 0:
            list.append(i)
    b = rng.choice(list)
    return a,b

