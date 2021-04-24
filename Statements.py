
# Here in this little program we see how can we work with statemens...
# IF, ELSE, ESLE IF, AND , OR
# Also we wrote a method which returns a result which is being given to exact parameter...
# And then we have printed it

male = True
short = False
answer = 50
answer1 = 20

def statement():
    if male != True:
        print("This person is woman")
        return  answer
    elif answer == 10:
        return 3
    elif answer > 10 and answer <20:
        return 1
    elif answer >10 or answer == 50:
        return "We have this ", 4
    else:
        if short == True:
            print("This person is short")
            answer1 = True
            return answer1
        else:
            return 0

result = statement()
print(result)

# Simple excercise
# GET THE LARGEST NUMBER AND PRINT IT

def myMaxNuber(num1, num2, num3):
    if num1 >=num2 and num1 >= num3:
        return num1
    elif num2>=num1 and num2 >= num3:
        return num2
    else:
        return num3


result = myMaxNuber(54,565,4)
print(result)




