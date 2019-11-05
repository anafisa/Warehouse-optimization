from import1 import waves, floors, wave_workers, wave_floor_route
from relocation1 import ordering1


def order(wave):

    global wave_workers, wave_floor_route
    workers = wave_workers[wave]
    k = workers//2
    tt = [[], [], [], []]
    res = []

    for i in range(1, k):
        for j in floors:
            routes = wave_floor_route[wave][j]
            tt[int(j)-1].append(max(ordering1(i, routes)))

    for i in range(len(tt[0])):
        for j in range(len(tt[1])):
            for g in range(len(tt[2])):
                for k in range(len(tt[3])):
                    if i+j+g+k+4 == workers:
                        res.append(max(tt[0][i], tt[1][j], tt[2][g], tt[3][k]))
    return min(res)


for wave in waves:
    print(order(wave))

