# num = int(input("Enter number:")) 
# sum = 0 
# count = 0 
# i = 1
# while count<num: 
#     if i%2==0:
#         sum = sum+i    
#         count = count+1
#     i+=1
# print(f"sum:{sum}")


# num = int(input("enter number:"))
# sum = 0
# ran = num*2 
# i = 1
# while i<=ran:
#     if i%2==0:
#         print(i)
#         sum = sum+i   
#     i+=1
# print(f"sum of:{sum}")

num = int(input("Enter number:"))
res = num*2
sum = 0
for i in range(1,res+1):
    if i%2==0:
        # print(i)
        sum = sum+i   
print(f"sum of:{sum}")