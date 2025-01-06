# num = int(input("Enter number:"))
# count = 0 
# i = 1 
# while i<=num:
#     if num%i==0:
#         count = count+1 
#     i = i+1
# if count==2:
#     print("Prime number")
# else:
#     print("Composite number")


num = int(input("Enter number:"))
count = 0 
for i in range(1,num+1):
    if num % i ==0:
        count = count+1 
    i = i+1 
if count == 2:
    print("Prie number")
else:
    print("Not a prime number")