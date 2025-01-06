# num = int(input("enter number:")) 
# sum = 0
# fix = num 
# while num>0:
#     sum = sum + (num%10)*(num%10)*(num%10)
#     num = num//10
# if sum == num: 
#     print(f"Give number is aramstrong number:{fix}")
# else:
#     print(f"Give number is not aramstrong number:{fix}")


num = input("enter number:")
sum = 0 
fixed = int(num)  
for i in num: 
    i = int(i) 
    sum = sum + (i%10)*(i%10)*(i%10)
if fixed == sum:
    print(f"Given Numer is aramstrong:{fixed}")
else:
    print(f"Given number is not aramstrong number:{fixed}")
