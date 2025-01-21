#123
#321

num = input("enter number:")
inVal = 0
for i in num:
    inVal = int(i) 
    inVal = (inVal*i)+(inVal/10)
    
print(inVal)