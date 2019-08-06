# Prompt for quote and an author Display the quote and author
# Use a single output statement to return this output using appropriate string escaping techniques
# Use concatenation instead of interpolation

while True:
    userQuoteInputPrompt = "Please enter a quote (type 'e' to exit)"
    userQuote = input(userQuoteInputPrompt)

    if len(userQuote) == 0:
        print("You did not enter any text")
    elif userQuote == "e":
        break
    else:
        print(userQuote)

        userAuthorInputPrompt = "Please enter the Author (type 'e' to exit)"
        userAuthor = input(userAuthorInputPrompt)

        if len(userAuthor) == 0:
            print("You did not enter any text")
        elif userAuthor == "e":
            break
        else:
            print(userAuthor)

            print(userAuthor + " says. \"" + userQuote + "\"")