import json
import numpy as np


data = None
with open('data_set') as f:
    data = json.load(f)
data_index = 0

DONE = 374

def get_next_data():
    idx = str(data_index)
    dist_list = []
    arriv_list = []
    index = 1
    tmp_list = []
    for item in data[idx]:
        if index % 5 == 0:
            dist_list.append(tmp_list)
            tmp_list = list()
            arriv_list.append(item)
        else:
            tmp_list.append(item)
        index += 1
    return dist_list, arriv_list

dist_data_set = []
arriv_data_set = []
for i in range(DONE):
    d, a = get_next_data()
    dist_data_set.append(d)
    arriv_data_set.append(a)
    data_index += 1

dist_data_set = np.array(dist_data_set)
arriv_data_set = np.array(arriv_data_set)


print(arriv_data_set)

