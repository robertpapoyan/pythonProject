# This is tbe way you are opening and saying what to do after opening
# r - read
# w - write
# a - add at the end anything
# r+ - all accesses
# open("MyFile.txt" "r")


file = open("MyFile.txt", "r")
if file.readable() == True:
    print(file.readable())
    # print(file.read())
    # print(file.read())
    # print(file.read())
    # print(file.read(3))


for i in file.readlines():
    print(i)
file.close()

file.write("Taza tox via script")