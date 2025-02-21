print("Welcome to the Blackjack Program")
import random

def deal_card ():
    '''Return a random card from the deck.'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    card = random.choice(cards)
    return card

user_card = []
computer_card = []
