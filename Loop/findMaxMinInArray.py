arr = [1,2,3,32,1323,31,233,21,23]
min = 0 
max = 0
for i in range(len(arr)):
    min = arr[i]
    if min<arr[i]:
        min=arr[i]
print(f"min value:{min}")

