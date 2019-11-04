from import1 import waves, floors, wave_workers, wave_floor_route
from route_time_calc import route_time, wave_time
from relocation1 import ordering1

wave = 25484
workers = wave_workers[wave]
print(workers)
k = workers//2

tt = [[], [], [], []]


for i in range(1, k):
    for j in floors:
        routes = wave_floor_route[wave][j]
        tt[int(j)-1].append(max(ordering1(i, routes)))


res = []

for i in range(len(tt[0])):
    for j in range(len(tt[1])):
        for g in range(len(tt[2])):
            for k in range(len(tt[3])):
                if i+j+g+k+4 == workers:
                    res.append(max(tt[0][i], tt[1][j], tt[2][g], tt[3][k]))

print(min(res))


