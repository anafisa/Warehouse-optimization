from data_import import waves, floors, wave_workers, wave_floor_route
from relocation1 import ordering1


def order(wave):

    workers = wave_workers[wave]
    k = workers//2
    tt = [[], [], [], []]
    res = []

    for i in range(1, k):
        for j in floors:
            routes = wave_floor_route[wave][j]
            tt[int(j)-1].append(max(ordering1(i, routes)))

    for i in range(1, len(tt[0])+1):
        for j in range(1, len(tt[1])+1):
            for g in range(1, len(tt[2])+1):
                for k in range(1, len(tt[3])+1):
                    if i+j+g+k == workers:
                        res.append(max(tt[0][i-1], tt[1][j-1], tt[2][g-1], tt[3][k-1]))

    return min(res)


for wave in waves:
    print(order(wave))


