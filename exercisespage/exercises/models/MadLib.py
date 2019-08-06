exit = False
while not exit:
    print("type 'e' to exit")

    userPrompt = "Please enter a "
    noun = "noun"
    verb = "verb"
    adjective = "adjective"
    adverb = "adverb"


    def validateUserInput(string):
        if len(string) == 0:
            print("You did not enter any text")
            return False
        elif string == "e":
            return False
        else:
            return True

    madLibArray = [noun, verb, adjective, adverb]

    for madLib in madLibArray:
        if madLib == "noun":
            noun = input(userPrompt+madLib)
            if not validateUserInput(noun):
                exit = True
                break
        elif madLib == "verb":
            verb = input(userPrompt+madLib)
            validateUserInput(verb)
            if validateUserInput(verb) == False:
                exit = True
                break
        elif madLib == "adjective":
            adjective = input(userPrompt+madLib)
            validateUserInput(adjective)
            if validateUserInput(adjective) == False:
                exit = True
                break
        elif madLib == "adverb":
            adverb = input(userPrompt+madLib)
            if validateUserInput(adverb) == False:
                exit = True
                break


    print("Do you {} your {} {} {}?".format(verb,adjective,noun,adverb))