
def calculation():
    number1 = float(input("Enter the first number: "))
    operator = input("Enter an operation")
    number2 = float(input("Enter the second number: "))

    if operator == "+":
        answer = number1 + number2
        return answer
    elif operator == "-":
        answer = number1 - number2
        return answer
    elif operator == "*":
        answer = number1 * number2
        return answer
    elif operator == "/":
        answer = number1 / number2
        return answer
    else:
        return "Incorrect operation, please, as operation, type in EITHER + OR - OR * OR /"


correctAnswer = calculation()
print(correctAnswer)