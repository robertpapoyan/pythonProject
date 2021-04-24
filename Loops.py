for i in range(10):
    print (i+1)


for val in "string":
    if val == "i":
        break
    print(val)

print("The end")


def evenNumbers(amount):
    for i in range(amount):
        print(i)
        if i % 2 == 0:
            print(i ,"is a even number")
        else:
            print(i, "is an odd number")


evenNumbers(10)

sequence = [1,2,8,100,200,'AAAA',"sdfsfsghyial", True]

for i in range(len(sequence)):
    if type(sequence[i]) == int:
        print("I am INTEGER and I am ", sequence[i])
    elif type(sequence[i]) == str:
        print("I AM STRIIIIIING " + sequence[i])
    else:
        print("I am different bitches", type(sequence[i]))

i = 0
while type(sequence[i]) != bool:
    print(type(sequence[i]))
    i = i + 1

print(sequence[i])


def expNum(base, pow):
    result = 1
    for i in range(pow):
        print(i)
        print(base, ".......................")
        result = result * base
    return result

print(expNum(3,2))




