# num = int(input("Enter number:"))
# i = 0 
# org = num 

# while num>0:
#     i = (i*10)+(num%10)
#     num = num//10

# print(i) 
# if i == org:
#     print("Given number is palendrom number:{}")
# else:
#     print("given number is not palendrom number")


# num = int(input("Enter number:")) 
# i = 0 
# orgNum = num 
# while num>0: 
#     i = (i*10)+(num%10)
#     num = num // 10 

# if i == orgNum:
#     print("True")
# else:
#     print("False")


num = input("ENter number:")
org = int(num)

rev = 0
intv = int(num)
for i in num:
    i = int(i) 
    rev = (rev*10)+(intv%10)
    intv = intv//10
print(rev)
if org == rev:
    print("True")
else:
    print("False") 