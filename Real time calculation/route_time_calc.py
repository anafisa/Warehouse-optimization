from data_import import waves, floors, route_cell_d, route_num, route_floor, wave_floor_route
from collections import defaultdict


wave_time = defaultdict(lambda: [])


def sshape(route_cell, route_num):

    r_time = dict()
    for route in route_cell:
        k = []
        for i in route_cell[route]:
            cell = list(map(int, i[1:-2].split("-")))
            if (cell[0] - 1) // 2 not in k:
                k.append((cell[0] - 1) // 2)

        dist = max(k) - min(k)
        p = len(k) + len(k) % 2

        if route_floor[route] == '1':
            r_time[route] = ((p * 27 + dist * 5.1) / 0.89
                             + route_num[route] * 2.37) / 60

        elif route_floor[route] == '3':
            r_time[route] = ((p * 24 + dist * 5.1) / 0.89
                             + route_num[route] * 2.37) / 60

        else:
            r_time[route] = ((p * 25.2 + dist * 5.1) / 0.89
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

