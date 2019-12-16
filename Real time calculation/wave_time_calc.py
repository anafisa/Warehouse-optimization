from data_import import wave_id, wave_id_num


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

    return (dist * 27 + sum(gate) * 5.1) / 0.89


def wave_time(wave_id, wave_id_num):

    time = []

    for key in wave_id.keys():
        res = []

        for i in wave_id[key].keys():
            res.append((sshape(wave_id[key][i]) + (sum(wave_id_num[key][i]) * 2.37))/60)

        time.append(max(res))

    return time


print(sum(wave_time(wave_id, wave_id_num))/60)


