# num = int(input("Enter number:"))
# i = 1 
# res = 1
# while i<=num:
#     res = res *i    
#     i+=1
# print(f"result:{res}")


num = int(input("Enter number:"))
res = 1 
for i in range(1,num+1):
    res = res*i    
print(f"Result:{res}")