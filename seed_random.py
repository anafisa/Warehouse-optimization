from data_import import wave_floor_box_cell, floors
from random import choice



def random_seed(aiseles):
    carriges = []
    boxes = list(aiseles.keys())
    k = len(boxes)//6
    boxes.sort(key=lambda key: len(aiseles[key]))
    boxes.reverse()


    for i in range(k):
        dist = dict()
        seed = choice(boxes)
        boxes.remove(seed)
        for i in boxes:
            dist[i] = len(aiseles[seed]-aiseles[i])
        keys = list(dist.keys())
        keys.sort(key=lambda key: dist[key])
        fit = keys[:5]
        [boxes.remove(i) for i in fit]
        fit.append(seed)
        carriges.append(fit)

    if boxes:
        carriges.append(boxes)
    return carriges


floor1 = random_seed(wave_floor_box_cell[25473]['1'])
floor2 = random_seed(wave_floor_box_cell[25473]['2'])
floor3 = random_seed(wave_floor_box_cell[25473]['3'])
floor4 = random_seed(wave_floor_box_cell[25473]['4'])

