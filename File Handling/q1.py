f = open("demofile.txt", "r")
c = 0
print("File content:")
print(f.read())
f.seek(0)
print("First two lines:")
print(f.readline())
print(f.readline())
f.seek(0)
print("First five characters:")
print(f.read(5))
f.close()