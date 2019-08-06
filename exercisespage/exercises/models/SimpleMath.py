# Prompt for two numbers
# Print the sum, difference, product and quotient
# keep math input and ouput seperate
# Single output statment

class MathObject:
    numberOne: int
    numberTwo: int

    def add(self, firstNumber, secondNumber):
      return firstNumber + secondNumber

    def subtract(self, firstNumber, secondNumber):
      return firstNumber - secondNumber

    def multiply(self, firstNumber, secondNumber):
      return firstNumber * secondNumber

    def divide(self, firstNumber, secondNumber):
      return int(firstNumber / secondNumber)

while True:
    userInput = MathObject()

    # Prompt FirstNumber
    userInput.numberOne = input("Please enter the first number (type 'e' to exit)")

    if userInput.numberOne == "e":
        break
    else:
        userInput.numberOne = int(userInput.numberOne)

    # Prompt second number
    userInput.numberTwo = input("Please enter the1 second number (type 'e' to exit)")

    if userInput.numberTwo == "e":
        break
    else:
        userInput.numberTwo = int(userInput.numberTwo)

    sumMath = str(userInput.add(userInput.numberOne, userInput.numberTwo))
    differenceMath = str(userInput.subtract(userInput.numberOne, userInput.numberTwo))
    productMath = str(userInput.multiply(userInput.numberOne, userInput.numberTwo))
    quotientMath = str(userInput.divide(userInput.numberOne, userInput.numberTwo))

    answersString = '''
    {firstNumber} + {secondNumber} = {sumMath}
    {firstNumber} - {secondNumber} = {differenceMath}
    {firstNumber} * {secondNumber} = {productMath}
    {firstNumber} / {secondNumber} = {quotientMath}
    '''.format(firstNumber=userInput.numberOne, secondNumber=userInput.numberTwo,
               sumMath=sumMath,
               differenceMath=differenceMath,
               productMath=productMath,
               quotientMath=quotientMath)

    print(answersString)




