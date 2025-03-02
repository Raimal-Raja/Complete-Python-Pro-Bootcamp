from gameData import data
import random
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

# Display logo
print(logo)
# Generate  a random account from the game data.
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_a = random.choice(data)
    
print(f'Compare A: {format_data(account_a)}')
print(vs)
print(f'Compare B: {format_data(account_b)}')