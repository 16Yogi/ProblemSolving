# question - print all even number range between 1 to 10 only  
list1 = []

for i in range(2,100,2):
  list1.append(i)
  list1Len = len(list1)
  # print(list1Len)
  if list1Len == 10:
    print(list1)
    break
  
