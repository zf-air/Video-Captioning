import os
import h5py
import numpy as np

#in_path = 'r2plus1d_34-tsp_on_activitynet-valid_features.h5'
in_path = 'r2plus1d_34-tsp_on_activitynet-test_features.h5'
#in_path = 'r2plus1d_34-tsp_on_activitynet-train_features.h5'
out_path = 'tsp'

if not os.path.exists(out_path):
    os.mkdir(out_path)

d = h5py.File(in_path)
for key in d.keys():
    v_d = d[key][:].astype('float32')
    np.save(os.path.join(out_path, key+'.npy'), v_d)