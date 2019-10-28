from import1 import wave_id, wave_floor_route, waves
from route_time_calc import route_time
from collections import defaultdict


def ordering1(workers, routes):
    d = dict()
    new_time = [0] * workers  # время, полученное с учетом нового распределения пик-рейсов, изначально список заполнен нулями
    time = []  # время каждого пик рейса
    new_ordering = defaultdict(lambda: [])


    for i in routes:
        d[route_time[i]] = i
        time.append(route_time[i])  # словарь вида время : пикрейс

    time = sorted(time, reverse=True)  # сортируем в обратном порядке

    while time:  # пока есть нераспределенные пик-рейсы
        for i in range(0, len(new_time)):
            if time:
                ind = new_time.index(min(new_time))
                new_time[ind] += time[0]
                time.remove(time[0])
            else:
                break
    return new_time


wave_workers = dict()
for i in wave_id.keys():  # составляю словарь волна : кол-во рабочих
    wave_workers[i] = len(wave_id[i].keys())



time = defaultdict(lambda: [])
f = ['1', '2', '3', '4']


for i in waves:
    for j in f:
        c = 0
        routes = wave_floor_route[i][j]
        for r in routes:
            c += route_time[r]
        time[i].append(c)  # находим время выполнения каждой волны


# print(time)
# print(wave_workers)


def floor_ordering(lst, n):
    s = sum(lst)
    d = s / n
    res = []
    for i in lst:
        res.append(round(i / d))
    if sum(res) > n:
        res[-1] -= 1
    return res


workers = []
for w in waves:
    workers.append(floor_ordering(time[w], wave_workers[w]))

# print(workers)


k = 0
res = []
final = []
for j in workers:
    for i in f:
            w = j[int(i)-1]
            routes = wave_floor_route[waves[k]][i]
            res.append(max(ordering1(w, routes)))
    final.append(max(res))
    res = []
    k += 1

print(final)
