file = open("tester7file.txt", "rb")
file.seek(5, 0)
print(file.read(5))

file.seek(3, 1)
print(file.read(5))

file.seek(-5, 2)
print(file.read())