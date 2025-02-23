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


def play_game():
    print(logo)
    print("Welcome to the number guessing game!")
    
    while True:
        level = input("Type '1' for easy or '2' for hard: ")
        if level in ['1', '2']:
            attempts = 10 if level == '1' else 5
            break
        print("Invalid level selected. Please choose 1 or 2.")

    number = random.randint(1, 100)
    print("\nI'm thinking of a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess the number.")

    for counter in range(attempts):
        attempts_left = attempts - counter
        print(f"\nYou have {attempts_left} attempts remaining.")
        
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess == number:
            print(f"\nCongratulations! You guessed the number {number}!")
            return True
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")

    print(f"\nGame Over! The number was {number}.")
    return False

def main():
    while True:
        play_game()
        while True:
            play_again = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
            if play_again in ['y', 'n']:
                break
            print("Invalid input! Please enter 'y' or 'n'.")
            
        if play_again == 'n':
            break

    print("\nThanks for playing!")

if __name__ == "__main__":
    main()