# num = int(input("Enter number:"))
# res = 0
# for i in range(1,num+1):
#     # print(i)
#     res = res+i   
#     print(res,end=" ") 
# print("Result:",res) 

# num = int(input("Enter number:")) 
# i = 0
# x = 0 
# y = 1
# while i<=num: 
#     print(i,end=" ") 
#     x = y 
#     y = i  
#     i = x+y 
#     # i+=1


num = int(input("enter number:"))
x = 1
y = 1 
for i in range(0,num):
    print(x,end=" ")
    temp = x+y 
    x = y  
    y = temp   

