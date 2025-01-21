import numpy as np
np1 = np.array([1,3,12,43,12,324,12])
val1 = np1[0]
val2 = []
for i in np1:
    if i > val1:
        val1 = i
        val2.append(val1) 
    print(f"i : {i} val1:{val1}")
print(val2[-2])
# for j in np1:
#     if j 