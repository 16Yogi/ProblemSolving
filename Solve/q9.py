import numpy as np   

arr = np.array([12,142,43,4,63,12,44])
arr2 = arr[0]

for i in arr:
    if i==arr2:
        arr2 = i   
        # print(arr2)
print(arr2)