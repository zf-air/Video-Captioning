import os

import numpy as np
import array

data_path = "c3d"
data_path1 = "tsp"
data_path2 = "tsn"

list0 = os.listdir(data_path)

list1 = os.listdir(data_path1)
list2 = os.listdir(data_path2)

i = 0
while i < 5:
    data = os.path.join(data_path, list0[i])
    loadData = np.load(data)
    print("----type----")
    print(type(loadData))
    print("----shape---")
    print(loadData.shape)
    print("----data----")
    print(loadData)

    data1 = os.path.join(data_path1, list1[i])
    loadData1 = np.load(data1)
    print("----type----")
    print(type(loadData1))
    print("----shape----")
    print(loadData1.shape)
    print("----data----")
    print(loadData1)

    data2 = os.path.join(data_path2, list2[i * 2])
    loadData2 = np.load(data2)
    print("----type----")
    print(type(loadData2))
    print("----shape----")
    print(loadData2.shape)
    print("----data----")
    print(loadData2)

    data3 = os.path.join(data_path2, list2[i * 2 + 1])
    loadData3 = np.load(data3)
    print("----type----")
    print(type(loadData3))
    print("----shape----")
    print(loadData3.shape)
    print("----data----")
    print(loadData3)
    i = i + 1