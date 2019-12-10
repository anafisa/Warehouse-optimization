from data_import import wave_floor_box_cell



def small_seed(aiseles):

    carts = []
    boxes_in_cart = 4

    boxes = list(aiseles.keys())
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


wave = 25483

floor1 = small_seed(wave_floor_box_cell[wave]['1'])
floor2 = small_seed(wave_floor_box_cell[wave]['2'])
floor3 = small_seed(wave_floor_box_cell[wave]['3'])
floor4 = small_seed(wave_floor_box_cell[wave]['4'])



# из  keys забираю к сиду 5 первых элементов, затем опять выбираю новый сид
# in order not to resort every time it is better to keep sorted elements and delete used boxes