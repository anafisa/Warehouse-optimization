from import1 import wave_workers, wave_floor_route, floors, waves
from route_time_calc import route_time
from collections import defaultdict

k = 0
res = []
final = []
workers = []
wave_time = defaultdict(lambda: [])


def ordering1(n, routes):
    """
    Функция, которая по распределению рабочих по этажам,формирует пик-рейсы.
    n - кол-во рабочих, работающих в определенную волну на определенном этаже по новому наспределению
    routes - пик-рейсы, которые выполняются в определенную волну на определенном этаже
    """

    d = dict()
    new_time = [0] * n  # время, полученное с учетом нового распределения пик-рейсов, изначально список заполнен нулями
    time = []  # время каждого пик рейса

    for i in routes:
        d[route_time[i]] = i  # словарь вида время : пикрейс
        time.append(route_time[i])

    time = sorted(time, reverse=True)

    while time:  # пока есть нераспределенные пик-рейсы
        for i in range(0, len(new_time)):
            if time:
                ind = new_time.index(min(new_time))
                new_time[ind] += time[0]
                time.remove(time[0])
            else:
                break
    return new_time


def floor_ordering(time_lst, n):
    """
    Функция распределения рабочих по этажам пропорционально времени.
    n - кол-во всех рабочих по волне,
    time_lst - список времени работы каждого этажа
    """
    s = sum(time_lst)
    d = s / n
    ordering = []
    for t in time_lst:
        ordering.append(round(t / d))
    if sum(ordering) > n:
        ordering[-1] -= 1
    return ordering


# находим время выполнения каждой волны на каждом этаже
for i in waves:
    for j in floors:
        c = 0
        routes = wave_floor_route[i][j]
        for r in routes:
            c += route_time[r]
        wave_time[i].append(c)

# распределяем рабочих по этажам
for w in waves:
    workers.append(floor_ordering(wave_time[w], wave_workers[w]))


for j in workers:
    for i in floors:
            w = j[int(i)-1]
            routes = wave_floor_route[waves[k]][i]
            res.append(max(ordering1(w, routes)))
    final.append(max(res))
    res = []
    k += 1

print(final)
