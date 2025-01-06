arr = [3,32,1323,31,2,1,233,21,23]
minV = arr[0]
for i in arr: 
    if i<minV:
        minV = i
print(f"Min value:{minV}")


maxV = arr[0]
for i in arr: 
    if i>maxV:
        maxV=i   
print(f"max value:{maxV}")
