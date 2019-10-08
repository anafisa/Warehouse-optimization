p = 5

for i in range(p):
    from random import choice
    from math import ceil
    from collections import defaultdict
    from pprint import pprint
    from import1 import wave_floor_id, wave_floor_route, route_cell_d, waves, wave_id, route_num
    from time_calculation import wave_time



    floors = [1, 2, 3, 4]

    nroute_cell = defaultdict(lambda: [])
    nid_nroute = defaultdict(lambda: nroute_cell.copy())
    wave_nid = defaultdict(lambda: nid_nroute.copy())

    nid_num = defaultdict(lambda: [])
    wave_nid_num = defaultdict(lambda: nid_num.copy())

    for i in waves:
        for j in floors:
            ids = wave_floor_id[i][f'{j}']
            routes = wave_floor_route[i][f'{j}']
            k = ceil(len(routes) / len(ids))
            ids = ids * k
            n = 0
            while routes:
                nroute = choice(routes)
                routes.remove(nroute)
                ncell = route_cell_d[nroute]
                wave_nid_num[i][ids[n]].extend(route_num[nroute])
                for g in range(len(ncell)):
                    cell = ncell[g]
                    wave_nid[i][ids[n]][nroute].append(list(map(int, cell[1:-2].split("-"))))
                n += 1

    print(wave_time(wave_nid, wave_nid_num))


# {wave1:{id1:[{route1:[cell1,cell2]}], id2}
