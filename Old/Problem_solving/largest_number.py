num1 = int(input("First value:"))
num2 = int(input("Second value:"))
num3 = int(input("third value:"))

if num1>num2 & num1>num3:
    print(f"{num1} is largest value")
elif num2>num1 & num2>num3:
    print(f"{num2} is largest value")
elif num3>num1 & num3>num2:
    print(f"{num3} is largest value")
else:
    print("invalid inputs")