import h5py
import numpy as np
from h5py import Dataset, Group, File
import torch

#data_path = "sub_activitynet_v1-3.c3d.hdf5"
data_path = "r2plus1d_34-tsp_on_workoutuow18-test_features.h5"

f = h5py.File(data_path, "r")

for k in f.keys():
    if f[k].name == '/a001_s001_e002':

      print(f[k][()])

f.close()
