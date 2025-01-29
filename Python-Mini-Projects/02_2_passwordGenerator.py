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

inputLetters = int(input('Enter number of letter you want: '))
inputSymbols = int(input("Enter number of Symbols you want: "))
inputNumbers = int(input("Enter number of numbers you want: "))


#easy  password
password = ''
for char in range(0, inputLetters):
    password += random.choice(letters)

for char in range(0, inputSymbols):
    password += random.choice(symbols)
    
for char in range(0, inputNumbers):
    password += random.choice(numbers)
print(password)

# hard password
password = []
for char in range(0, inputLetters):
    password += random.choice(letters)

for char in range(0, inputSymbols):
    password += random.choice(symbols)
    
for char in range(0, inputNumbers):
    password += random.choice(numbers)
random.shuffle(password)
password = ''.join(password)
print(password)