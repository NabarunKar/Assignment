import os

if os.path.exists("delete.txt"):
    print("File has been deleted.")
    os.remove("delete.txt")
else:
    print("The file does not exist")