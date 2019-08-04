#Output contains user's input
#Use single statement to construct the output
#Use built in language function to dtermine number of chars

while True:
    userInputPrompt = "Please enter some text and I will tell you how many characters you entered (type 'e' to exit)"
    userInput = input(userInputPrompt)

    if len(userInput) == 0:
        print("You did not enter any text")
    elif userInput == "e":
        break
    else:
        print("Your text of '{}' has {} characters".format(userInput, len(userInput)))


