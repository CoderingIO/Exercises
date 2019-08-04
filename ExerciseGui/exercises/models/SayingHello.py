# keep input, string concatenation, and ouput seperate
# different greetings for different people

while True:
    nameInputString = "Please Enter your name (type 'e' to exit)"
    userName = input(nameInputString)
    feelings =""


    if userName == "Harry":
        feelings = "awful"
    elif userName == "e":
        break
    else:
        feelings = "good"

    greetingString = "{} it is {} to see you.".format(userName, feelings)

    print(greetingString)
