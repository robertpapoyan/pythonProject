
# Every "dzaynavor" translates to symbol *
def translation(phrase):
    translator = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translator = translator + "*"
        else:
            translator = translator + letter
    return  translator

result = translation(input("Please enter any phrase: "))

print(result)






