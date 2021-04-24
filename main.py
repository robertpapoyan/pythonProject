# Here we are going to start learning the syntax of
#               THIS FUNCKING DISGUSTING LANGUAGE

# First hello world function
def printItOut ():
    print("Hello world I am in Python Now")

# SImpe work with different types of variables
# Parisng adding and printing
def simpleWorkFithDataTypes():
    userName = "Robert Papoyan"
    userAge = "25"
    text = "Type in any number:  "

    yourAgeIs = input(text)

    sum = int(userAge) + int(yourAgeIs)
    print(sum)
    int(sum)
    str(userAge)
    str(yourAgeIs)
    print("The summ of our ages is: ",yourAgeIs,"+",userAge," = ",sum)

# Simple work with lists
def simpleWorkWithSimpleLists():

    name1 = "aaa"
    number1 = 322
    name2 = "sadasd"
    number2 = 123.3

    list1 = [name1,number1, name2,number2]
    print(list1)
    print(list1[1:])

    list1[1] = 787988789
    print(list1)

# simpleWorkWithSimpleLists()
# simpleWorkFithDataTypes()
# printItOut()



