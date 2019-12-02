from data_import import wave_floor_box_cell


def big_seed(aiseles):

    carts = []
    boxes_in_cart = 6

    boxes = list(aiseles.keys())
    cart_num = len(boxes)//boxes_in_cart
    boxes.sort(key=lambda key: len(aiseles[key]))
    boxes.reverse()

    for i in range(cart_num):
        dist = dict()
        seed = boxes[0]
        del boxes[0]

        for i in boxes:
            dist[i] = len(aiseles[seed]-aiseles[i])

        keys = list(dist.keys())
        keys.sort(key=lambda key: dist[key])

        fit = keys[:boxes_in_cart-1]
        [boxes.remove(i) for i in fit]
        fit.append(seed)
        carts.append(fit)

    if boxes:
        carts.append(boxes)

    return carts


wave = ''

floor1 = big_seed(wave_floor_box_cell[wave]['1'])
floor2 = big_seed(wave_floor_box_cell[wave]['2'])
floor3 = big_seed(wave_floor_box_cell[wave]['3'])
floor4 = big_seed(wave_floor_box_cell[wave]['4'])
