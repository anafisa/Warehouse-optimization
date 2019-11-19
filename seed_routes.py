from import1 import wave_floor_box_cell


data = wave_floor_box_cell[25472]['4']

keys = list(data.keys())



def my_flatten(arr, res=None):

    if res == None:
        res = []

    for item in arr:
        if type(item) == int:
            res.append(item)
        else:
            my_flatten(item, res)

    return res


def form_route(box):
    global keys
    route = [box]
    iter = 1
    for i in keys:
        if (data[i] & data[box] == data[i] or data[i] & data[box] == data[box]) and iter != 6:
            iter += 1
            route.append(i)
            keys.remove(i)
    return route


def form_rest_route(box):
    global kk
    route = [box]
    iter = 1
    for i in kk:
        if data[i] & data[box] != {} and iter != 6:
            iter += 1
            route.append(i)
            kk.remove(i)
    return route

carrige = []
bag = []
while keys:
    box = keys[0]
    del keys[0]
    res = form_route(box)
    if len(res) == 6:
        carrige.append(res)
    else:
        bag.append(res)

kk = my_flatten(bag)
carrige.extend(bag)

print(carrige)
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



