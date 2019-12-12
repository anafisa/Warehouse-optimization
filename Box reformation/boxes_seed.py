from data_import import wave_floor_order_code_volume, wave_floor_order_code_num, order_code_aisle


orders = wave_floor_order_code_volume[25472]['1']
q = wave_floor_order_code_num[25472]['1']

# print(orders)

box1 = 13200
box2 = 26400
box3 = 42000


def form_box(orders, quantity, order_code_aisle):

    new_boxes = []
    item_num = []

    for order in orders:
        cap = 0
        total_num = 0
        batch = []
        aisles_set = set()
        goods = list(orders[order].keys())
        goods.sort(key=lambda key: order_code_aisle[order][key])

        while goods:
            item = goods[0]
            a = order_code_aisle[order][item]
            val = orders[order][item]
            num = quantity[order][item]

            if cap + val < 42000:
                cap += val
                total_num += num
                batch.append(item)
                goods.remove(item)
                aisles_set.add(a)

            else:
                new_boxes.extend([batch])
                item_num.append([aisles_set, total_num])

                cap = 0
                total_num = 0
                batch = []
                aisles_set = set()

    f = sorted(item_num, key=lambda key: len(key[0]))
    ais = []
    item = []
    for i in f:
        ais.append(i[0])
        item.append(i[1])
            # можно посмотреть new_boxes
    ais.reverse()
    item.reverse()

    return [ais, item]


wave = 25472

floor1 = form_box(wave_floor_order_code_volume[wave]['1'], wave_floor_order_code_num[wave]['1'], order_code_aisle)
floor2 = form_box(wave_floor_order_code_volume[wave]['2'], wave_floor_order_code_num[wave]['2'], order_code_aisle)
floor3 = form_box(wave_floor_order_code_volume[wave]['3'], wave_floor_order_code_num[wave]['3'], order_code_aisle)
floor4 = form_box(wave_floor_order_code_volume[wave]['4'], wave_floor_order_code_num[wave]['4'], order_code_aisle)





