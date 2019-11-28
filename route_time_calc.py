from import1 import waves, floors, route_cell_d, route_num, wave_floor_route, route_floor
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

        if route_floor[route] == '1':
            r_time[route] = (((len(k)+1) * 27 + (len(k) - 1) * 5.1) / 0.89
                                + route_num[route] * 2.37) / 60

        elif route_floor[route] == '3':
            r_time[route] = (((len(k)+1) * 24 + (len(k) - 1) * 5.1) / 0.89
                             + route_num[route] * 2.37) / 60
        else:
            r_time[route] = (((len(k)+1) * 25.2 + (len(k) - 1) * 5.1) / 0.89
                             + route_num[route] * 2.37) / 60

    return r_time


route_time = sshape(route_cell_d, route_num)
# print(route_time[1187705])
# print(route_time[1189361])
# print(route_time[1189711])
# print(route_time[1189722])




for i in waves:
    for j in floors:
        c = 0
        routes = wave_floor_route[i][j]
        for r in routes:
            c += route_time[r]
        wave_time[i].append(c)

# print(wave_time)
#  r_time[route] = ((len(k) * 27 + (max(k) + 1) * 5.1) / 0.89
#                             + route_num[route] * 2.37) / 60