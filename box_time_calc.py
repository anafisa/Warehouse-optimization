from import1 import box_cell_d, box_num


def box_time(boxes):
    cell = []
    k = []
    num = 0

    for i in boxes:
        cell.extend(box_cell_d[i])
        num += box_num[i]

    for c in cell:
        if (c - 1) // 2 not in k:
                k.append((c - 1) // 2)
    time = ((len(k) * 30  + max(k) * 5) / 0.87
                         + num * 2.37) / 60
    return time


