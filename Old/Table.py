# val1 = int(input("first value:"))
# val2 = int(input("Second value:"))
val1 = 1
val2 = 11

for i in range(val1,val2):
  print(f"Table of {val1}")
  for j in range(val1,val2):
    print(f"{i} x {j}: {i*j}")
  print()