# str1 = input("Str1:")
# print(str1)
# print(str1.upper())

str1 = input("str1:")
str2 = ""
for i in str1:
    if 'a'<=i<='z':
        str2+=chr(ord(i)-32)
    else:
        str2+i
print(str1)
print(str2)