import numpy as np
import os
from scipy import io

def read_xyz(file, max_body=1, num_joint=20):
    mat = io.loadmat(file)
    mat_t = np.transpose(mat['one_sample'])
    numFrame = mat['one_sample'].shape[0]
    data = np.zeros((3, numFrame, num_joint, max_body))
    m = 0
    for n in range(numFrame):
        for j in range(num_joint):
            if m < max_body and j < num_joint:
                # m代表body数量 一直不变，为0   j代表关节点数量，为20个
                # n代表帧数
                data[:, n, j, m] = [mat_t[j * 3][n], mat_t[j * 3 + 1][n], mat_t[j * 3 + 2][n]]
            #    if np.any(np.isnan(data)) == True:
             #       print(file)
            else:
                pass
    return data
