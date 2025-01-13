# arr = [12,321,2333,1,12,12]
# mn = arr[0]

# for i in arr:
#     if mn>i:  
#         mn = i   
# print(mn)

    
# import numpy as np 
# arr = np.array([12,231,123,21,3,213,123,1])
# mn = arr[0]
# for i in range(len(arr)):
    # if mn > arr[i]:
        # mn = arr[i]
# print(mn)



import numpy as np   

arr = np.array([32,13,232,4,13,2,421])
mn = arr[0]
i = 0 
while i<len(arr):
    if mn>arr[i]:
        mn = arr[i]
    i+=1
print(f"min value:{mn}")