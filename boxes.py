from import1 import num_boxes
from collections import defaultdict

keys = num_boxes.keys()
res = defaultdict(lambda: 0)

for i in keys:
    num = len(list(num_boxes[i]))
    res[num] += 1

print(res)