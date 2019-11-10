from import1 import waves, floors, wave_workers, wave_floor_route
from route_time_calc import route_time, wave_time
from relocation1 import ordering1



def order(k):
    global wave_workers, floor
    return k * wave_workers[wave] // len(floors)


def rel(t):
    tt = []
    global floors, wave_floor_route
    for i in floors:
        routes = wave_floor_route[wave][i]
        tt.append(max(ordering1(t[int(i)-1], routes)))
    return tt


def ordering2(wave):

    global floors,  wave_floor_route

    sh = [1] * len(floors)
    rem = wave_workers[wave] % len(floors)

    g = wave_time[wave].index(max(wave_time[wave]))

    t = list(map(order, sh))
    t[g] += rem
    tt = rel(t)

    res = []
    for g in range(10):
        c1 = tt.index(max(tt))
        c2 = tt.index(min(tt))
        t[c1] += 1
        t[c2] -= 1
        tt = rel(t)
        res.append(max(tt))
    return min(res)


for wave in waves:
    print(ordering2(wave))

