f = open("demofile.txt", "a")
f.write("We have added a new line to the file!")
f.close()
f = open("demofile.txt", "r")
print(f.read())