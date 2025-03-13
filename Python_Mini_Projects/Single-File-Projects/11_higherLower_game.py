from gameData import data
import random
import os
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


def format_data(account):
    '''Format the account data into printable format'''
    accountName = account['name']
    accountDesc = account['description']
    accountCountry = account['country']
    return f'{accountName}, a {accountDesc}, from {accountCountry}'

def checkAnswer(guess, aFollowers,  bFollowers):
    """Take the  user guess and follower counts and returns if they got it right. """
    if aFollowers > bFollowers:
        return guess == 'a'
    else:
        return guess == "b"
            
        
# Display logo
print(logo)
score = 0
gameShouldContinue = True
account_b = random.choice(data)
while gameShouldContinue:
# Generate  a random account from the game data.
    # account_a = random.choice(data)
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_a = random.choice(data)
    
    print(f'Compare A: {format_data(account_a)}')
    print(vs)
    print(f'Compare B: {format_data(account_b)}')

    # ask the user for a guess
    guess = input("Who has more followers ? Type 'A' or 'B':").lower()

    aFollowerCount = account_a['follower_count']
    bFollowerCount = account_b["follower_count"]

    is_correct = checkAnswer(guess, aFollowerCount, bFollowerCount)

    os.system('cls')
    print(logo)
    if is_correct:
        score+=1
        print(f'You are right! Current score: {score}')
        
    else:
        print(f"Sorry!, that's wrong. Final score: {score}")
        gameShouldContinue = False