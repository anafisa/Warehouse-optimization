from import1 import wave_id, wave_id_num

def sshape(wave_dict):
    dist = 0
    gate = []
    for cell in wave_dict.values():
        k = []

        for i in cell:
            if (i[0] - 1) // 2 not in k:
                k.append((i[0] - 1) // 2)
        gate.append(max(k) - min(k))
        dist += len(k)
    return (dist * 30 + sum(gate) * 5)/0.87





