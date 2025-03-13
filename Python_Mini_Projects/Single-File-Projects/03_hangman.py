import random

stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)
words = ["madhu", "tara", "sitara"]

choosenWord = random.choice(words)
lives = 6
display = []
for char in choosenWord:
    display += "_"

counter = len(choosenWord)
# winner = 0
while counter > 0:
    guessLetter = input('Guess the letter: ').lower()
    # for index,letter in enumerate(choosenWord):
    #     if letter == guessLetter:
    #         print('Right')
    #         # winner += 1
    #         display[index] =  letter 
    #     else:
    #         print("wrong")
    for position in range(len(choosenWord)):
        letter = choosenWord[position]
        if letter ==  guessLetter:
            display[position] = letter
            lives -= 1
    counter -= 1
    print(stages[lives])
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
