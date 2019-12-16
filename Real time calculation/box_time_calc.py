from data_import import box_cell_d, box_num, box_floor


def box_time(boxes):

    floor = box_floor[boxes[0]]
    cell = []
    k = []

    s = 60
    num = 0
    v = 0.89
    len1 = 27
    len2 = 25.2
    len3 = 24
    width = 5.1
    item_time = 2.37

    for i in boxes:
        cell.extend(box_cell_d[i])
        num += box_num[i]

    for c in cell:
        c = list(map(int, c[1:-2].split("-")))
        if (c[0] - 1) // 2 not in k:
            k.append((c[0] - 1) // 2)

    dist = max(k) - min(k)
    p = len(k) + len(k) % 2

    if floor == '1':
        time = ((p * len1 + dist * width) / v
                + num * item_time) / s

    elif floor == '3':
        time = ((p * len3 + dist * width) / v
                + num * item_time) / s
    else:
        time = ((p * len2 + dist * width) / v
                + num * item_time) / s
    return time


