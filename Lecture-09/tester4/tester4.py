# "r" (read) mode
file = open("tester4.txt","r")
content = file.read()
print(content)


# "w" (write) mode
file = open("tester4.txt","w")
file.write("abc\nxyz")
file = open("tester4.txt","r")
content = file.read()
print(content)


# "w" (write) mode
file = open("tester4.txt","a")
file.write("jklvvw")
file.writelines("jkl\nvvw")
file = open("tester4.txt","r")
content = file.read()
print(content)