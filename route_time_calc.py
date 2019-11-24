from import1 import waves, floors, route_cell_d, route_num, wave_floor_route
from collections import defaultdict

wave_time = defaultdict(lambda: [])  # время выполнения каждой волны


def sshape(route_cell, route_num):
    r_time = dict()
    for route in route_cell.keys():
        k = []
        for i in route_cell[route]:
            cell = list(map(int, i[1:-2].split("-")))
            if (cell[0] - 1) // 2 not in k:
                k.append((cell[0] - 1) // 2)
        r_time[route] = ((len(k) * 30 + max(k) * 5) / 0.87
                         + route_num[route] * 2.37) / 60
    return r_time


route_time = sshape(route_cell_d, route_num)


for i in waves:
    for j in floors:
        c = 0
        routes = wave_floor_route[i][j]
        for r in routes:
            c += route_time[r]
        wave_time[i].append(c)

