import re

str1 = "hello this is my string"
# res1 = re.search("this",str1)
# res1 = re.search("this *string$",str1)
# res1 = re.findall("s",str1)
# res1 = re.split("\s",str1)
res1 = re.sub("\s","9",str1)
if res1:
    print("Hey..!")
    print(res1)
else:
    print("Bey..!")

