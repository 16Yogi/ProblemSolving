import numpy as np  

arr = np.array([12,32,321,24,31,45,1,54,23])
arr2 = np.array([],dtype=int)
for i in arr:
    if i%2==0:
        arr2 = np.append(arr2,i)
print(arr2)