import random
letters = [
    'a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z','A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z'
]
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '_','\\', '|','?', '`', '~'
    ]

numbers = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]

welcomeMessage = input('Welcome to password generator 😊\nPlease hit enter and provide some details below!')

inputLetter = int(input("Enter number of letters"))
inputSymbol = int(input("Enter numbber of Symbol"))
inputNumber = int(input("Enter number of numbers"))
indexOfLetters =[]
for i in range (0, inputLetter):
    index = random.randint(i,len(symbols))
    indexOfLetters.append(index)

indexOfSymbols =[]
for i in range(0,inputSymbol):
    index = random.randint(i,len(symbols))
    indexOfSymbols.append(index)
indexOfNumber =[]
for i in range(0, inputNumber):
    index = random.randint(i,len(numbers))
    indexOfNumber.append(index)

passwordLetter = []
for index in indexOfLetters:
    letter = letters[index]
    passwordLetter.append(letter)
    
passwordSymbol = []
for index in indexOfSymbols:
    symbol = symbols[index]
    passwordSymbol.append(symbol)
passwordNumber = []
for index in indexOfNumber:
    number = numbers[index]
    passwordNumber.append(number)
    
password = passwordLetter + passwordNumber + passwordSymbol
random.shuffle(password)

final_Password = ''.join(password)
print(final_Password)