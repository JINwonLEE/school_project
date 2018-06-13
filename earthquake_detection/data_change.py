import scipy.io
import numpy as np
import sys

file_name = sys.argv[1]


data = scipy.io.loadmat(file_name)

name = file_name.split(".")

for i in data:
    if '__' not in i and 'readme' not in i:
        np.savetxt((name[0]+".csv"),data[i],delimiter=',')
