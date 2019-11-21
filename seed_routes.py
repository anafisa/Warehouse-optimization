from import1 import wave_floor_box_cell


data = wave_floor_box_cell[25472]['1']

keys = list(map(list, data.values()))
keys.sort(key=len)
# print(keys)
print(len(keys)//6)


def my_flatten(arr, res=None):

    if res == None:
        res = []

    for item in arr:
        if type(item) == int:
            res.append(item)
        else:
            my_flatten(item, res)

    return res


def form_carriers(keys):
    keys.sort(key=len)
    bag = []
    lst = []
    while keys:
        box = keys[-1]
        iter = 1
        carrige = [keys[-1]]
        del keys[-1]
        m = keys
        for j in m:
            if iter != 6:
                if set(j) & set(box) == set(j):
                    carrige.append(j)
                    keys.remove(j)
                    iter += 1
            else:
                lst.append(carrige)
                break
        if iter < 6:
            for i in carrige:
                bag.append(i)
    return [lst, bag]



c = form_carriers(keys)
new = c[1]
k = form_carriers(new)
print(form_carriers(k[1]))

#  если больше не получается нормальных распределений, то применяем ещё раз к багу наш алг и оставляем как есть
# нужно из обрывков нормальных распределений сформировать итоговое решение или как то переделать функцию, что все это будет происходить в цикле 

# print(form_carriers(new))







#
#
# def form_route(box):
#     global keys
#     route = [box]
#     iter = 1
#     for i in keys:
#         if (data[i] & data[box] == data[i] or data[i] & data[box] == data[box]) and iter != 6:
#             iter += 1
#             route.append(i)
#             keys.remove(i)
#     return route
#
#
# def form_rest_route(box):
#     global kk
#     route = [box]
#     iter = 1
#     for i in kk:
#         if data[i] & data[box] != {} and iter != 6:
#             iter += 1
#             route.append(i)
#             kk.remove(i)
#     return route
#
#
# carrige = []
# bag = []
# while keys:
#     box = keys[0]
#     del keys[0]
#     res = form_route(box)
#     if len(res) == 6:
#         carrige.append(res)
#     else:
#         bag.append(res)
#
# kk = my_flatten(bag)
# carrige.extend(bag)
#
# print(carrige)
# b = []
# while kk:
#     box = kk[0]
#     del kk[0]
#     res = form_rest_route(box)
#     if len(res) == 6:
#         carrige.append(res)
#     else:
#         b.append(res)
#
# carrige.extend(b)
# print(carrige)



