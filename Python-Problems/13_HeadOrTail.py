import random
# test_seed = int(input("Create a seed number: "))

# random.seed(test_seed)

choice  = input("Head or Tail? ")
tossCoin = random.randint(0,1)
if tossCoin == 0:
    coin = "Head"
else:
    coin = "Tail"
print("The result is:", coin)
if choice == coin:
    print("You guessed correctly!")
else:
    print("You guessed incorrectly!")