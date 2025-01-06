# num = int(input("enter number:"))
# sum = 0 
# while num>0:
#     sum = sum + num%10 
#     num = num//10 
# print(f"sum of:{sum}")


num = input("enter:")
sum = 0 
for i in num:
    i = int(i)
    sum = sum+i%10
    i = i//10 
print("sum of:",sum) 