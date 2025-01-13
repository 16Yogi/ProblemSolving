num = 1
for i in range(4):
    for j in range(0+i):
        print(" ",end="")
    for k in range(4-i):
        print(num,end="")
        num+=1
    print("")