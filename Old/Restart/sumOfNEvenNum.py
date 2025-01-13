# num = int(input("Enter a value:")) 
# i = 1 
# sum = 0
# while i<=num:
#     if i%2==0:
#         sum = sum+i   
#     i+=1
# print("sum of even:",sum)

num = int(input("enter:"))
sum = 0
for i in range(1,num+1):
    if i%2==0:
        sum = sum+i  
print(sum)