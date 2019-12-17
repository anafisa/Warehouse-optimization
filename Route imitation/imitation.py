from data_import import wave_floor_id, wave_floor_route, floors
from route_time_calc import route_time
from collections import defaultdict


def ordering(workers, routes):

    d = dict()
    new_time = [0] * len(workers)
    time = []
    new_ordering = defaultdict(lambda: [])

    for i in routes:
        d[route_time[i]] = i
        time.append(route_time[i])

    time = sorted(time, reverse=True)

    while time:
        for i in range(0, len(new_time)):
            if time:
                ind = new_time.index(min(new_time))
                new_time[ind] += time[0]
                new_ordering[workers[ind]].append(d[time[0]])
                time.remove(time[0])
            else:
                break

    return [new_time, new_ordering]


keys = wave_floor_route.keys()
res = [[], [], [], [], [], [], []]

for j in floors:
    c = 0
    for i in keys:
        workers = wave_floor_id[i][j]
        routes = wave_floor_route[i][j]
        res[c].append(max(ordering(workers, routes)[0]))
        c += 1

a = list(map(max, res))

print(a)
