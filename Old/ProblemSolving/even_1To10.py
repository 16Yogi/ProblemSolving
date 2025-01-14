list1 = []
for i in range(1,100):
  if i%2==1:
    list1.append(i)
    list1Len = len(list1)
    if list1Len == 10:
      print(list1)
      break