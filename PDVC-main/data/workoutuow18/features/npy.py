import numpy as np

data_path = 'tsp/v_a001_s001_e001.npy'

loadData = np.load(data_path)

print(loadData.shape)

print(loadData)