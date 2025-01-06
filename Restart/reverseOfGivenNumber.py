# num = int(input("Enter number:"))

# for i in range(num,0,-1):
#     print(i)  

# num = int(input("Enter number:"))
# i = 0 
# while num>0:
#     i = (i*10)+(num%10)
#     num = num//10 
# print(i)


# num = int(input("Enter number:"))
# i = 0
# while num>0:
#     i = (i*10)+(num%10)
#     num = num//10 
# print(i)

# num = input("enter number:")
# for i in range(len(num)-1,-1,-1):
#     print(num[i],end="")    
 

num = input("ENter number:")
rev = 0
intv = int(num)
for i in num:
    i = int(i) 
    print
    rev = (rev*10)+(intv%10)
    intv = intv//10
print(rev)