print("Welcome to the Blackjack Program")
import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

                                      
     
print(logo)
def deal_card ():
    '''Return a random card from the deck.'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """take a list of cards and return the score calculate from from the card"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "Win the a BlackJack"
    elif user_score > 21:
        return "you went over. You Lose"
    elif computer_score ==21:
        return "opponent went over. You Win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
    
def play_game():
    user_card = []
    computer_card = []
    is_game_over = False
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
        
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"Your card: {user_card}, current score: {user_score}")
        print(f"Computer first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input('Type "Y" to get another card, or "N" to pass: ')
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
        
    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
        
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") =='y':
    os.system('cls')
    play_game()