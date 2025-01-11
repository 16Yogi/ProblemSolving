# arr = [12,32,123,123,21312434,1231,34]
# max = arr[0]
# for i in arr:
#     if i>max:
#         max = i
# print(max)


# import numpy as np  
# arr = np.array([12,32,123,123,21312434,1231,34])
# mx = arr[0]
# for i in range(len(arr)):
    # if arr[i]>mx:
        # mx = arr[i]
# print(mx)
        

arr = [12,32,123,123,21312434,1231,34]
i = 0 
mx = arr[0]

while i<len(arr):
    if mx<arr[i]:
        mx = arr[i]
    i+=1
print(mx)