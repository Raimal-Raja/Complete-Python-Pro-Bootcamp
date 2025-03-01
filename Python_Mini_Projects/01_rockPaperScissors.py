import random
print("Welcome to Rock, Paper, Sciessors game! Cipher")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]
userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(images[userInput])

computer_choice = random.randint(0,2)
print(images[computer_choice])

if userInput > 3 or userInput < 0:
    print('You have typed invalid number. You lose!')
elif userInput == 0 and computer_choice == 2:
    print('You chose "Rock", Computer Chose "Scissors".You win!')
elif userInput > computer_choice:
    print('You chose "Paper" Computer chose "Rock". You Win!')
elif computer_choice > userInput:
    print("You chose 'Rock', Computer chose 'Paper'. You lose!")
elif computer_choice == userInput:
    print("You both chose same, It's a draw!")
else:
    print("You chose 'Scissor', Computer chose 'Rock', You lose!")
  