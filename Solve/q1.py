import numpy as np 

arr = np.array([12,1,23,21])
# sum = 0
# for i in arr:
#     sum = sum+i
#     # print(i)
# print(f'Result:{sum}')


i = 0
sum = 0 
while i<len(arr):
    sum = sum+arr[i]
    i+=1
print(f'Sum of:{sum}')
    