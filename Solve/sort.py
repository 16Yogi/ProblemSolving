arr = [12, 35, 1, 10, 34, 1]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>=arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)