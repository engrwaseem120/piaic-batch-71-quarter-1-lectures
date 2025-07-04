file = open("tester5file.txt", "r")
content = file.read()
print(content)


file = open("tester5file.txt", "r")
file.seek(10)
content = file.read()
print(content)

file = open("tester5file.txt", "r")
file.seek(15)
content = file.read()
print(content)


file = open("tester5file.txt", "r")
file.seek(18 + 7)
current_position = file.tell()
print(current_position)