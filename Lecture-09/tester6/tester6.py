file = open("tester6file.txt", "r")
content = file.readline()
print(content)

content = file.readline()
print(content)


file = open("tester6file.txt", "r")
lines = file.readlines()
for line in lines:
    print(line)


file = open("tester6file.txt", "r")
for line in file:
    print(line)