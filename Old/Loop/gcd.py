lenth = int(input("Enter how digits you want to enter:"))
gcdDigit = []
gcdVal = []
for i in range(lenth):
    gcdNum = int(input(f"Enter value {i+1}:"))
    gcdDigit.append(gcdNum)
# print(gcdDigit)

for j in gcdDigit:
    for k in range(1,len(gcdDigit)+1):
        count += k   
        if j%count==0:
            gcdVal.append(count)

print(gcdVal)