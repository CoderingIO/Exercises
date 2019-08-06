class AreaOfRectangularRoom:
    length: float
    width: float
    area: float

    def calculateArea(self):
        return self.width * self.length


# Console app
while True:
    userInput = AreaOfRectangularRoom()
    # Prompt FirstNumber
    userInput.length = input("Please enter the first number (type 'e' to exit)")

    if userInput.length == "e":
        break
    else:
        userInput.length = float(userInput.length)

    # Prompt second number
    userInput.width = input("Please enter the1 second number (type 'e' to exit)")

    if userInput.width == "e":
        break
    else:
        userInput.width = float(userInput.width)

    userInput.area = userInput.calculateArea()

    print(userInput.area)