# num = int(input("Enter number:"))
# res = 0
# for i in range(1,num+1):
#     if i%2==1:
#         res = res+i
#         # print(i) 
# print(f"Result:{res}")

num = int(input("Enter number:"))
i = 1
res = 0
while num>=i:
    if i%2==1:
        res = res+i 
    # print(i)
    i+=1
print(f"Result:{res}")