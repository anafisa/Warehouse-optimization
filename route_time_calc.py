from import1 import waves, floors, route_cell_d, route_num, wave_floor_route, route_floor
from collections import defaultdict


wave_time = defaultdict(lambda: [])  # время выполнения каждой волны


def sshape(route_cell, route_num):
    r_time = dict()
    last = 0
    for route in route_cell.keys():
        k = []
        for i in route_cell[route]:
            cell = list(map(int, i[1:-2].split("-")))
            if (cell[0] - 1) // 2 not in k:
                k.append((cell[0] - 1) // 2)
                last = cell[1]
        if route_floor[route] == '1':
           r_time[route] = ((len(k) * 27 + (max(k) + 1) * 5.1 + last * 0.9) / 0.89
                            + route_num[route] * 2.37) / 60
        elif route_floor[route] == '3':
            r_time[route] = ((len(k) * 24 + (max(k) + 1) * 5.1 + last * 0.6) / 0.89
                             + route_num[route] * 2.37) / 60
        else:
            r_time[route] = ((len(k) * 25.2 + (max(k) + 1) * 5.1 + last * 0.63) / 0.89
                             + route_num[route] * 2.37) / 60


    return r_time


route_time = sshape(route_cell_d, route_num)
print(route_time[1187785])
print(route_cell_d[1187785])


for i in waves:
    for j in floors:
        c = 0
        routes = wave_floor_route[i][j]
        for r in routes:
            c += route_time[r]
        wave_time[i].append(c)

print(wave_time)

