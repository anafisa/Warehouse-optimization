import pandas as pd
import pprint as pp
from openpyxl import load_workbook
from collections import defaultdict

wb = load_workbook('data.xlsx')
sheet = wb['Лист1']

route_cell = defaultdict(lambda: [])
id_route = defaultdict(lambda: route_cell.copy())
wave_id = defaultdict(lambda: id_route.copy())
id_num = defaultdict(lambda: [])
wave_id_num = defaultdict(lambda: id_num.copy())

'''
{wave1:{id:[{route:[cell]}], id2},wave2:{id:{route:cell}}} 
'''

for i in range(1, 55432):
    wave = sheet.cell(row=i, column=2).value
    id = sheet.cell(row=i, column=9).value
    route = sheet.cell(row=i, column=10).value
    cell = sheet.cell(row=i, column=12).value
    num = sheet.cell(row=i, column=5).value

    wave_id[wave][id][route].append(list(map(int, cell[1:-2].split("-"))))
    wave_id_num[wave][id].append(num)


# pp.pprint(wave_id)
# print(wave_id.keys())
# print(sum(wave_id_num[25472][13]))


def wave_max_dist(wave_dict):
    dist = 0
    gate = []
    for cell in wave_dict.values():
        k = []

        for i in cell:
            if (i[0] - 1) // 2 not in k:
                k.append((i[0] - 1) // 2)
        gate.append(max(k) - min(k))
        dist += len(k)
    return (dist * 30 + sum(gate) * 5  )/0.87


# print(wave_time(wave_id[25472][41]))
# print(len(wave_time(wave_id[25472])))


for key in wave_id.keys():
    res = []
    for i in wave_id[key].keys():
        res.append([(wave_max_dist(wave_id[key][i]) + (sum(wave_id_num[key][i])*2.37))/60, i])
    print(max(res))

