# what is natural number ?
# A natural number is a postive integer starting from 1 and increasing by increments of 1 (1,2,3,4,5)

# Q- Print natural number between 1 to 10

# val1 = int(input("start to :"))
# val2 = int(input("End to :"))
val1 = 1
val2 = 100
list1 = []

for i in range(val1,val2):
  # print(i)
  list1.append(i)
  # print(list1)
  list1Len = len(list1)
  # print(list1Len)
  
  if list1Len == 10:
    print(list1)
    break
  
# print(list1)