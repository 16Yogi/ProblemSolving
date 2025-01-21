num = int(input("Enter number:"))
sum = 0
# for i in range(1,num+1):
    # sum = sum+i
    # print(i,end=" ")
# print(f"Result:{sum}")

i = 1
while i<=num:
    sum = i+sum   
    i+=1 

print(f"Sum of :{sum}")