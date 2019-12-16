from data_import import wave_floor_order_code_volume, wave_floor_order_code_num, order_code_aisle


def form_box(orders, quantity, order_code_aisle):

    box = "here should be volume"
    item_num = []
    new_boxes = []

    for order in orders:

        pre = -1
        cap = 0
        total_num = 0
        batch = []

        aisles_set = list()
        goods = list(orders[order].keys())
        goods.sort(key=lambda key: order_code_aisle[order][key])

        while goods:
            item = goods[0]
            a = order_code_aisle[order][item]
            val = orders[order][item]
            num = quantity[order][item]

            if cap + val < box and (a - pre < 1 or pre == -1):
                pre = a
                cap += val
                total_num += num
                aisles_set.append(a)
                batch.append(item)
                goods.remove(item)

            else:
                new_boxes.extend([batch])
                item_num.append([set(aisles_set), total_num])
                pre = -1
                cap = 0
                total_num = 0
                batch = []
                aisles_set = list()

        if total_num != 0:
            item_num.append([set(aisles_set), total_num])

    f = sorted(item_num, key=lambda key: len(key[0]))
    ais = []
    item = []

    for i in f:
        ais.append(i[0])
        item.append(i[1])

    ais.reverse()
    item.reverse()

    # you also may return new_boxes

    return [ais, item]


wave = "*****"

floor1 = form_box(wave_floor_order_code_volume[wave]['1'], wave_floor_order_code_num[wave]['1'], order_code_aisle)
floor2 = form_box(wave_floor_order_code_volume[wave]['2'], wave_floor_order_code_num[wave]['2'], order_code_aisle)
floor3 = form_box(wave_floor_order_code_volume[wave]['3'], wave_floor_order_code_num[wave]['3'], order_code_aisle)
floor4 = form_box(wave_floor_order_code_volume[wave]['4'], wave_floor_order_code_num[wave]['4'], order_code_aisle)







