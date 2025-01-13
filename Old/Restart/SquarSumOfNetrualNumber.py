# num = int(input("Enter value:"))
# sum = 0
# i = 1 
# while i<=num:
#     sum = sum+(i*i)  
#     i+=1

# print(f"Square Sum of num {num} is :{sum}")

num = int(input("Enter:"))
sum = 0
for i in range(1,num+1):
    sum = sum+(i*i)   
print("Square sum of:",sum)