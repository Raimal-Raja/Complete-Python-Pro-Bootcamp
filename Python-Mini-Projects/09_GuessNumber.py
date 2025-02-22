import random
import os

logo = '''
   _____                       _   _            _   _                 _                 
  / ____|                     | | | |          | \ | |               | |                
 | |  __ _   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
'''

print(logo)
attempts = 0
counter = 0
level = int(input("Welcome to number guess game.\nType '1' for easy: \nType '2' for hard: "))

should_continue = True
while should_continue:
    if level == 1:
        attempts = 10
    elif level == 2:
        attempts = 5
    else:
        print("Invalid level selected.")
        break
    
    number = random.randint(1, 100)
    counter = 0  # Reset counter for each new game
    
    while counter < attempts:  # Changed <= to < to fix attempt counting
        guess_number = int(input('Guess the number: '))
        
        if guess_number > number:
            print('Too high!')
        elif guess_number < number:
            print('Too low!')
        elif guess_number == number:
            print("Congratulations! You Guess it!")
            break
            
        counter += 1
        
        if counter == attempts:  # Move this check here to show message only once
            print(f"You ran out of attempts! The correct number was: {number}")
    
    should_play = input('Do you want to play again? Type "y" or "n": ').lower()
    if should_play == 'n':
        should_continue = False  # Fixed to actually end the game
    elif should_play != 'y' and should_play != 'n':
        print('Invalid input! Please enter valid command.')
        continue
        
    if should_continue:  # Only show this if continuing
        print(logo)
        level = int(input("Welcome to the number guessing game!\nType '1' for easy: \nType '2' for hard: "))

print("Thanks for playing!")