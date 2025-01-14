import numpy as np  

arr = np.array([12,312,31,4,21,12,5,34,5,23,6,4,6])
num = int(input("enter number:"))
count = 0
for i in arr:
    if i == num: 
        count+=1
print(count)
