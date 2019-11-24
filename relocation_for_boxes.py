from box_time_calc import box_time
from import1 import wave_workers
from WM_to_Py import floor1, floor2, floor3, floor4


def time(floor):
    answ = []
    for i in floor:
        t = box_time(i)
        answ.append(t)
    return answ


tt1 = time(floor1)
tt2 = time(floor2)
tt3 = time(floor3)
tt4 = time(floor4)

time_lst = [tt1, tt2, tt3, tt4]

def ordering1(n, time_list):

    new_time = [0] * n
    t = sorted(time_list, reverse=True)

    while t:
        for i in range(0, len(new_time)):
            if t:
                ind = new_time.index(min(new_time))
                new_time[ind] += t[0]
                t.remove(t[0])
            else:
                break
    return new_time


def order(wave, time):

    workers = wave_workers[wave]
    k = workers//2
    tt = [[], [], [], []]
    res = []

    for i in range(1, k):
        for j in range(4):
            t = time[j]
            tt[j].append(max(ordering1(i, t)))

    for i in range(len(tt[0])):
        for j in range(len(tt[1])):
            for g in range(len(tt[2])):
                for k in range(len(tt[3])):
                    if i+j+g+k+4 == workers:
                        res.append(max(tt[0][i], tt[1][j], tt[2][g], tt[3][k]))
    return min(res)


print(order(25472, time_lst))



