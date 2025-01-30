import random
words = ["madhu", "tara", "sitara"]

choosenWord = random.choice(words)

display = []
for char in choosenWord:
    display += "_"

counter = len(choosenWord)
# winner = 0
while counter > 0:
    guessLetter = input('Guess the letter: ').lower()
    for index,letter in enumerate(choosenWord):
        if letter == guessLetter:
            print('Right')
            # winner += 1
            display[index] =  letter 
        else:
            print("wrong")
    counter -= 1
    print(display)
# if winner == len(choosenWord):
if not '_' in display:
    print("You Win")
#     print("You Win")
# else:
#     print('You lose!')
else:
    print('You lose!')
display = ''.join(display)
print(display)
