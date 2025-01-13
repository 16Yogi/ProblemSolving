n = int(input("End of number:"))
evNum = []
sum = 0
for i in range(1,n+1):
    if i %2==0:
        evNum.append(i) 
# print(evNum)
for i in evNum:
    sum = sum+i
print(evNum) 
print(f"Sum of even number:{sum}")