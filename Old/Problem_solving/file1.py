f = open("test.txt","r")
# print(f.read())  #print all the line
# print(f.read(5)) #print only given number character

# read line function
# print(f.readline()) #read only one line
print(f.readline(5)) #read only five charater of test.txt file

# print all which in test.txt using loop
# for i in f:
    # print(i) 

f.close() 