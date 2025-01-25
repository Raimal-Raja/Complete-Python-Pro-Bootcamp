print("Welcome to the Love Calculator! ")
yourName = input("Enter your name: ")
yourPatner = input("Enter your patner's name: ")

# string = ""


# try this method #############
# yourName.lower()
# yourPatner.lower()

# countTrueYour = (yourName.count('t')) + (yourName.count('r')) + (yourName.count('u')) + (yourName.count('e'))
# countTruePatner = (yourPatner.count('t')) + (yourPatner.count('r')) + (yourPatner.count('u')) + (yourPatner.count('e'))
# countloveYour = (yourName.count('l')) + (yourName.count('o')) + (yourName.count('v')) + (yourName.count('e'))
# countLovePatner = (yourPatner.count('l')) + (yourPatner.count('o')) + (yourPatner.count('v')) + (yourPatner.count('e'))

# trueCount = countTrueYour + countTruePatner
# loveCount = countloveYour + countLovePatner
# love = str(trueCount) + str(loveCount)
####################

# second method

combineBothNames = yourName + yourPatner
lowerCaseString = combineBothNames.lower()

t = lowerCaseString.count('t')
r = lowerCaseString.count('r')
u = lowerCaseString.count('u')
e = lowerCaseString.count('e')

true = t + r + u + e

l = lowerCaseString.count('l')
o = lowerCaseString.count('o')
v = lowerCaseString.count('v')
e = lowerCaseString.count('e')

love = l + o + v + e

loveScore = str(true) + str(love) 
# print(f"your love score is {loveScore}")

loveScore = int(loveScore)

if loveScore < 10 or loveScore > 90:
    message = f"Your Score is {loveScore}, you go together!"
elif loveScore > 40 and loveScore < 50:
    message = f"Your Score is {loveScore}, you are alright together!"
else:
    message = f"Your Score is {loveScore}"
    
print(message)