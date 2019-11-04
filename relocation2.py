from import1 import waves, floors, wave_workers, wave_floor_route
from route_time_calc import route_time, wave_time
from relocation1 import ordering1

wave = 25484
sh = [1] * len(floors)
num = wave_workers[wave]//len(floors)
rem = wave_workers[wave]%len(floors)


def order(k):
    global num
    return k*num


g = wave_time[wave].index(max(wave_time[wave]))

t = list(map(order, sh))
t[g] += rem
print(t)



def rel(t):
    tt = []
    global floors, wave, wave_floor_route
    for i in floors:
        routes = wave_floor_route[wave][i]
        tt.append(max(ordering1(t[int(i)-1], routes)))
    return tt


tt = rel(t)
print(tt)

for g in range(10):
    c1 = tt.index(max(tt))
    c2 = tt.index(min(tt))
    t[c1] += 1
    t[c2] -= 1
    tt = rel(t)
    print(tt)
    print(max(tt))




