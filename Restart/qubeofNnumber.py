# num = int(input("enter number:"))
# sum = 0
# for i in range(1,num+1):
#     sum = sum+(num*num*num)
# print(f"Qube sum:{sum}")


num = int(input("Enter number:"))
sum = 0 
i = 1 
while i<=num:
    sum = sum + (i*i*i)  
    i+=1 
print(f"Sum of {sum}")