list1 = []
list2 = []
for i in range(1,100):
  list1.append(i)
  list1Len = len(list1)
  if list1Len == 10:
    print("Normal:",list1)
    # list1.reverse()
    # print("Reverse function:",list1)
    for j in list1:
      list2.insert(0,j)
      
print(f"Reverse:{list2}")
      
 
    
  