from import1 import wave_floor_box_cell, floors


def form_carriges(data, boxes):  # data – словарь коробка: множество ячеек, множество коробок по нужному этажу
    boxes.sort(key=lambda key: len(data[key]))
    d = boxes
    bag = []
    lst = []
    while d:
        box = data[d[-1]]
        carrige = [d[-1]]
        del d[-1]
        iter = 1
        elem = d
        for j in elem:
            if iter != 6:
                if data[j] & box == data[j]:
                    carrige.append(j)
                    d.remove(j)
                    iter += 1
            else:
                lst.append(carrige)
                break
        if iter < 6:
            for i in carrige:
                bag.append(i)
    return [lst, bag]


def form_bag(data, boxes): #data – словарь коробка: множество ячеек
    boxes.sort(key=lambda key: len(data[key]))
    d = boxes
    bag = []
    lst = []
    while d:
        box = data[d[-1]]
        carrige = [d[-1]]
        del d[-1]
        iter = 1
        elem = d
        for j in elem:
            if iter != 6:
                if len(data[j] & box) - len(data[j]) <= 2:
                    carrige.append(j)
                    d.remove(j)
                    iter += 1
            else:
                lst.append(carrige)
                break
        bag.append(carrige)
    return bag


def route_floor(data):
    boxes = list(data.keys())
    carrige = form_carriges(data, boxes)
    result = []

    while carrige[0]:
        result.extend(carrige[0])
        carrige = form_carriges(data, carrige[1])

    bag = carrige[1]
    f = form_bag(data, bag)
    result.extend(f)

    return result


d = wave_floor_box_cell[25472]['1']
for i in floors:
    print(route_floor(wave_floor_box_cell[25472][i]))


