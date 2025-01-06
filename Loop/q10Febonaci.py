num = int(input("Enter number:"))
i = 0
x = 0
y = 1
while i<=num:
    print(i) 
    x = y 
    y = i   
    i = x+y 
    