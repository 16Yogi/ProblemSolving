# row = 5
# for i in range(row,0,-1):
#     print(str(i)*i)

row = 5
for i in range(row,0,-1):
    for j in range(5-i):
        print(" ",end="")
    for k in range(row,0,-1):
        print("",end="")
    print(str(i)*i)