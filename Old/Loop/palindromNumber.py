num = int(input("Enter a number:"))
rev = 0 
org = num 
while num > 0:
    rev = (rev*10)+(num%10)
    num = num//10 

if rev == org:
    print(f"Given Number is palendrom number:{org}")
else:
    print(f"Give number is not a palendrom Number:{org}")
