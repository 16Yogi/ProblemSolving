import numpy as np   

arr1 = np.array([12,1,4,12,43])
arr2 = np.array([2,122,22,121])
small1 = arr1[0]
small2 = arr2[0]
allSmallVal = 0
for i in arr1:
    if i < small1:
        small1 = i   
# print(small1)
for j in arr2:
    if j < small2:
        small2 = 2
# print(small2)

if small1<small2:
    # print(small1)
    allSmallVal = small1
elif small2<small1:
    # print(small2)
    allSmallVal = small2

print(allSmallVal)

margArr = arr1+arr2 
print(margArr)