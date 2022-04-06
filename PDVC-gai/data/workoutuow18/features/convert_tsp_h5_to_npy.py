import os
import h5py
import numpy as np

#in_path = 'tsp-18-16/r2plus1d_18-tsp_on_workoutuow18-valid_features.h5'
#in_path = 'tsp-18-16/r2plus1d_18-tsp_on_workoutuow18-test_features.h5'
in_path = 'tsp-18-16/r2plus1d_18-tsp_on_workoutuow18-train_features.h5'
#in_path = 'test.h5'
out_path = 'tsp'

if not os.path.exists(out_path):
    os.mkdir(out_path)

d = h5py.File(in_path)
for key in d.keys():
    v_d = d[key][:].astype('float32')
    name = 'v_' + key
    np.save(os.path.join(out_path, name+'.npy'), v_d)