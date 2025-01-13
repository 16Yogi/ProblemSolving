str1 = input("Str1:")  
str2 = ""

for i in str1:
    if 'A' <= i <= 'Z':
        str2 += chr(ord(i) + 32)
    else:
        str2 += i
print(str1)
print(str2)
