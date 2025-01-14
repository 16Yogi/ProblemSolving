# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# x = 8
# list1 = []
# list2 = []
# res = 1
# res2 = 1
# for i in range(1,x+1):
#     print(i)
#     list1.append(i)

# for j in list1:
#     res = res*j
# print(res)

# for k in list1:
#     list2.insert(0,k)
# print(list2)
# for l in list2:
#     print(l)
#     res2 = res2*l
# # print(res)
# print(res2)
# --------------------

# list1 = []
# list2 = []
# for i in range(1,5+1):
#     # print(i)
#     list1.append(i)
# for j in list1:
#     print(j)
#     list2.insert(0,j)
# print(list2)
# print("-------------------")

# list3 = []
# list4 = []
# res = 1
# for k in range(1,5+1):
#     list3.append(k)
# for l in list3:
#     res = res * l
# print(res)



def fun(x):
    if x==0:
        return 1
    return x * fun(x-1)
print(fun(5))

