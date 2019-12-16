from data_import import wave_floor_box_cell


def big_seed(boxes, aiseles):

    carts = []
    boxes_in_cart = 4

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


def small_seed(boxes, aiseles):

    carts = []
    boxes_in_cart = 6

    k = len(boxes)//boxes_in_cart
    boxes.sort(key=lambda key: len(aiseles[key]))

    for i in range(k):
        dist = dict()
        seed = boxes[0]
        del boxes[0]

        for i in boxes:
            dist[i] = len(aiseles[i]-aiseles[seed])

        keys = list(dist.keys())
        keys.sort(key=lambda key: dist[key])

        fit = keys[:boxes_in_cart-1]
        [boxes.remove(i) for i in fit]
        fit.append(seed)
        carts.append(fit)

    if boxes:
        carts.append(boxes)
    return carts


def seed_mixed(aiseles):

    proportion = 5
    num = len(aiseles)
    a = list(aiseles.keys())

    big = big_seed(a[:num//proportion], aiseles)
    small = small_seed(a[num//proportion:], aiseles)
    big.extend(small)

    return big
    

wave = ''

floor1 = seed_mixed(wave_floor_box_cell[wave]['1'])
floor2 = seed_mixed(wave_floor_box_cell[wave]['2'])
floor3 = seed_mixed(wave_floor_box_cell[wave]['3'])
floor4 = seed_mixed(wave_floor_box_cell[wave]['4'])


