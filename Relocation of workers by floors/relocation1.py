from data_import import waves, floors, wave_workers, wave_floor_route
from route_time_calc import route_time, wave_time


def ordering1(n, routes):
    """
    Функция, которая по распределению рабочих по этажам,формирует пик-рейсы.
    n - кол-во рабочих, работающих в определенную волну на определенном этаже по новому распределению
    routes - пик-рейсы, которые выполняются в определенную волну на определенном этаже
    """
    d = dict()
    new_time = [0] * n
    time = []

    for i in routes:
        d[route_time[i]] = i
        time.append(route_time[i])

    time = sorted(time, reverse=True)

    while time:
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


k = 0
res = []
final = []
workers = []

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

# print(final)
