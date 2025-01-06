# num = input("Enter numbers:")
# count = 0
# for i in num:
#     count +=1
# print(f"Count of {num} given digit:{count}")


num = int(input("Enter:"))
count = 0
while num>0:
    num = num // 10
    count+=1
print(count)