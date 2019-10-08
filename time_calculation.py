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
    return (dist * 30 + sum(gate) * 5 )/0.87


def wave_time(wave_id, wave_id_num):
    time = []
    for key in wave_id.keys():
        res = []
        for i in wave_id[key].keys():
            res.append([(sshape(wave_id[key][i]) + (sum(wave_id_num[key][i]) * 2.37))/60, i])  # calculate time (min)
        time.append(max(res))  # choose the worst res in every wave
    return time  # among all waves choose one with the worst res


#print(wave_time(wave_id, wave_id_num))
