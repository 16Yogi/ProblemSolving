import numpy as np   

arr = np.array([1,2,12,43,12,34,12,50])
max = arr[0]
# for i in arr:
#     if max < i:
#         max = i   
# print(f"max value:{max}") 

i = 0
while i < len(arr):
    if max < arr[i]:
        max = arr[i] 
    i+=1
print(f'max:{max}')