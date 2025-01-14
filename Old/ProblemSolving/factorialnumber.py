#factorial
# what is factorial number
# Ans- A factorial number is maltiplay by self value range
# Example- 5! = 5 × 4 × 3 × 2 × 1 = 120

num1 = 5
list1 = []
list2 = []
result = 1
for i in range(1,num1+1):
  list1.append(i)
for j in list1:
  list2.insert(0,j)

l2Len = len(list2)
# print(l2Len)

# user rever
for k in list2:
  # print(k)
  result *=  k 
print(f"using revers:{result}")


# for l in list1:
#   result = result * l 
# print(f"without reverse:{result}")
  
# print(l)
  
  
  
