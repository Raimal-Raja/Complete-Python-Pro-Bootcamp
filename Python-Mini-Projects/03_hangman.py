import random
words = ["madhu", "tara", "sitara"]

randomChoose = random.choice(words)

display = []
for char in randomChoose:
    display += "_"

guessLetter = input('Guess the letter').lower()
for index,letter in enumerate(randomChoose):
    if letter == guessLetter:
        print('Right')
        display[index] =  letter 
    else:
        print("wrong")
print(display)
