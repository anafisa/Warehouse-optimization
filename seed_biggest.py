from data_import import wave_floor_box_cell


def big_seed(aiseles):

    carriges = []
    boxes_in_carrige = 6

    boxes = list(aiseles.keys())
    carriges_num = len(boxes)//boxes_in_carrige
    boxes.sort(key=lambda key: len(aiseles[key]))
    boxes.reverse()

    for i in range(carriges_num):
        dist = dict()
        seed = boxes[0]
        del boxes[0]

        for i in boxes:
            dist[i] = len(aiseles[seed]-aiseles[i])

        keys = list(dist.keys())
        keys.sort(key=lambda key: dist[key])

        fit = keys[:boxes_in_carrige-1]
        [boxes.remove(i) for i in fit]
        fit.append(seed)
        carriges.append(fit)
    if boxes:
        carriges.append(boxes)
    return carriges


floor1 = big_seed(wave_floor_box_cell[]['1'])
floor2 = big_seed(wave_floor_box_cell[]['2'])
floor3 = big_seed(wave_floor_box_cell[]['3'])
floor4 = big_seed(wave_floor_box_cell[]['4'])

