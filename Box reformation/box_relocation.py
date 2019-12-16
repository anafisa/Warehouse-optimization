from to_carts import f1, f2, f3, f4
from relocation_for_carts import order


def box_time(aisles_num, floor):

    ais = aisles_num[0]
    quantity = aisles_num[1]
    total_time = []

    # parms
    s = 60
    v = 0.89
    len1 = 27
    len2 = 25.2
    len3 = 24
    width = 5.1
    item_time = 2.3

    for i in range(len(ais)):

        cell = ais[i]
        num = quantity[i]

        dist = max(cell) - min(cell)
        p = len(cell) + len(cell) % 2

        if floor == '1':
            time = ((p * len1 + dist * width) / v
                    + num * item_time) / s

        elif floor == '3':
            time = ((p * len3 + dist * width) / v
                    + num * item_time) / s
        else:
            time = ((p * len2 + dist * width) / v
                    + num * item_time) / s

        total_time.extend([time])

    return total_time


b1 = box_time(f1, '1')
b2 = box_time(f2, '2')
b3 = box_time(f3, '3')
b4 = box_time(f4, '4')


time_lst = [b1, b2, b3, b4]


print(order("*****", time_lst))
