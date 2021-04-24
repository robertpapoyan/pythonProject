file = open("MyFile.txt", "a")

file.write("\n Taza tox via script")

file.close()

file = open("MyFile.txt", "r")

for i in file:
    print(i)

file.close()