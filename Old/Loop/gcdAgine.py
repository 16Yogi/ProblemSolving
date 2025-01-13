len1 = int(input("Enter lenght:"))
i = 1
gcdNUm = []
count = 1
while i<=len1:
    num = int(input(f"Enter number {i}:"))
    if num%count==0:
        gcdNUm.append(count)
    count+=1 