from import1 import wave_floor_id, wave_floor_route
from route_time_calc import route_time
from collections import defaultdict

def ordering(workers, routes):
    d = dict()
    new_time = []  # время, полученное с учетом нового распределения пик-рейсов
    [new_time.append(0) for i in range(len(workers))]  # изначально список заполнен нулями
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
                new_ordering[workers[ind]].append(d[time[0]])
                time.remove(time[0])
            else:
                break
    return [new_time, new_ordering]

# print(ordering(workers, routes))


keys = wave_floor_route.keys()
res = [[],[],[],[],[],[],[]]
f = ['1', '2', '3', '4']
k = list(keys)



for j in f:
    c = 0
    for i in keys:
        workers = wave_floor_id[i][j]
        routes = wave_floor_route[i][j]
        res[c].append(max(ordering(workers, routes)[0]))
        c += 1
a = list(map(max, res))
# print(a)
b = list(map(min, res))
c = []
[c.append(a[i]-b[i]) for i in range(len(a))]
print(c)


for i in range(len(c)):
    if c[i] > 10:
        wave = k[i]
        print(wave, res[i].index(min(res[i]))+1, res[i].index(max(res[i]))+1)





