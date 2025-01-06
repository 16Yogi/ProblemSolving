# num = int(input("Enter number:"))
# val = 1
# while num>0:
#     val = val*(num%10)
#     num = num//10 
# print(val)


num = int(input("Enter number:")) 
val = 1 
for i in range(1,num+1):
    val = val*i   
print(f"Product result:{val}")