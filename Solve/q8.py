import numpy as np   

arr1 = np.array([12,31,2,3212,2,12])
arr2 = np.array([23,32,12,31,21,31]) 

# for i in arr1:
#     for j in arr2:
#         if i == j:
#             print(i) 

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            print(arr1[i])

count1 = 0 
count2 = 0 

for i in range(len(arr1)):
    count1+=1
for j in range(len(arr2)):
    count2+=1

if i == j:
    print("Both are have equle length")
else:
    print("False length")
        