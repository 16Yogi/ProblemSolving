num = int(input("Enter number:"))
fact = 1 

for i in range(1,num+1):
    print(f"{fact} = {fact} * {i}")
    fact = fact*i    
print(f"fact:{fact}")