import numpy as np   

arr = np.array([11,22,33,44,55])
# print(arr)
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end=" ")

len1 = len(arr)
i = 0
while len1>0:
    i = (i*10)+(arr[len1]%10)
    arr[len1] = arr[len1]//10 
print(i)
    
