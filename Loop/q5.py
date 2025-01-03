userInt = int(input("For fact number:"))
fact = 1
for i in range(1,userInt+1):
    # print(i)
    fact = fact*i 
print(f"Factorial of {userInt}:{fact}")