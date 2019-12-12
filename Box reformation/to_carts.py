from data_import import wave_floor_box_cell
from boxes_seed import floor1, floor2, floor3, floor4



def form_carts(ais, item):

    boxes_in_cart = 6
    carts = []
    quantity = []
    n = len(ais)//boxes_in_cart

    for k in range(n):
        seed = ais[0]
        num = item[0]
        ais.remove(seed)
        item.remove(num)
        cart = seed
        test = ais.copy()
        test.sort(key=lambda key: len(key-seed))

        for i in range(0, boxes_in_cart - 1):
            cart |= test[i]
            ind = ais.index(test[i])
            num += item[ind]
            ais.remove(ais[ind])
            item.remove(item[ind])

        carts.append(cart)
        quantity.append(num)

    last_cart = set()

    if ais:
        for i in ais:
            last_cart = last_cart | i
        carts.append(last_cart)
        quantity.append(sum(item))

    return [carts, quantity]


# print(sum(floor1[1]))

f1 = form_carts(floor1[0], floor1[1])
f2 = form_carts(floor2[0], floor2[1])
f3 = form_carts(floor3[0], floor3[1])
f4 = form_carts(floor4[0], floor4[1])
