import h5py
import numpy as np
from h5py import Dataset, Group, File
import torch

#data_path = "sub_activitynet_v1-3.c3d.hdf5"
data_path = "r2plus1d_34-tsp_on_activitynet-valid_features.h5"

f = h5py.File(data_path, "r")

for k in f.keys():
    print(f[k])
#    print(f[k].name)
#    print(f[k][()])

f.close()
