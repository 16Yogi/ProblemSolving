import numpy as np 

arr = np.array([1,2,3,4,5])
sum = 0
# for i in arr:
    # sum = sum+i     
# print(f"Sum of array:{sum}")

len1 = len(arr)
# print(len1)
i = 0
while len1>i:
    # print(arr[i])
    sum  = sum+arr[i]
    i+=1
print(f"Sum of arry:{sum}")