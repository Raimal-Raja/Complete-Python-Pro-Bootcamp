import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
should_continue = True
auction = {}
while should_continue:
    name = input('Please enter name: ')
    bid = int(input('Please enter price $:'))
    auction[name] = bid 
    answer = input("is there anyone else want to bid? type yes or no: ")
    if answer == "no":
        should_continue = False
    if answer == "yes":
        os.system('cls')
highest_bid = 0
winner = ''

for bidder in auction:
    if auction[bidder] > highest_bid:
        highest_bid = auction[bidder]
        winner = bidder
print(f"the winner is {bidder} with highest bid {highest_bid}")