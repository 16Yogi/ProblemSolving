import numpy as np    
arr = np.array([23,1,42,31,3,312])
min = arr[0]
# for i in arr:
#     if i<min:
#         min = i   
# print(f"min value:{min}")

i = 0 
while i<len(arr):
    if arr[i]<min:
        min = arr[i]
    i+=1
print(f"min value:{min}")