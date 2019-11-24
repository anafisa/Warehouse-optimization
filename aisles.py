from import1 import wave_floor_box_cell
from box_time_calc import box_time


data = wave_floor_box_cell[25472]['1']
d = list(data.keys())

if len(d) % 6 == 0:
    num_box = len(d)//6
else:
    num_box = (len(d)//6) + 1


b_time = dict()


for i in d:
    b_time[i] = box_time([i])



boxes = sorted(b_time, key=lambda key: b_time[key])
boxes.reverse()


carriges = []
[carriges.append([]) for i in range(num_box)]
time = [0] * num_box


while boxes:
    box = boxes[0]
    boxes.remove(box)
    ind = time.index(min(time))
    carriges[ind].append(box)
    time[ind] += b_time[box]

print(carriges)
print(time)
