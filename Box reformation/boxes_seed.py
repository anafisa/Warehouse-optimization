from data_import import wave_floor_order_code_volume, wave_floor_order_code_num, order_code_aisle


def form_box(orders, quantity, order_code_aisle):

    box = 42000
    # new_boxes = []
    item_num = []

    for order in orders:  # пробегаем по номерам прставок
        pre = -1
        cap = 0
        total_num = 0
        # batch = []
        aisles_set = list()
        goods = list(orders[order].keys())  # goods это список всех кодов товаров данного заказа
        goods.sort(key=lambda key: order_code_aisle[order][key])  # сортируем по

        while goods:  # пока есть необработанные коды
            item = goods[0]  # seed равен 1 эл
            a = order_code_aisle[order][item]  # полчучаем номер прохода
            val = orders[order][item]
            num = quantity[order][item]  # получаем кол-во товаров соотв определенному коду

            #  проверить какой а тип данных

            # разница с предыдущим

            if cap + val < box and (a - pre < 2 or pre == -1):
                pre = a
                cap += val  # заполняем коробку
                total_num += num  # добавляем к кол-ву
                aisles_set.append(a)  # добавляем мн-во проходов
                # batch.append(item)  # добавляем товар в коробку
                goods.remove(item)  # удаляем из

            else:
                # new_boxes.extend([batch])
                item_num.append([set(aisles_set), total_num])
                pre = -1
                cap = 0
                total_num = 0
                # batch = []
                aisles_set = list()

        if total_num != 0:
            item_num.append([set(aisles_set), total_num])

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


wave = 25486

floor1 = form_box(wave_floor_order_code_volume[wave]['1'], wave_floor_order_code_num[wave]['1'], order_code_aisle)
floor2 = form_box(wave_floor_order_code_volume[wave]['2'], wave_floor_order_code_num[wave]['2'], order_code_aisle)
floor3 = form_box(wave_floor_order_code_volume[wave]['3'], wave_floor_order_code_num[wave]['3'], order_code_aisle)
floor4 = form_box(wave_floor_order_code_volume[wave]['4'], wave_floor_order_code_num[wave]['4'], order_code_aisle)








