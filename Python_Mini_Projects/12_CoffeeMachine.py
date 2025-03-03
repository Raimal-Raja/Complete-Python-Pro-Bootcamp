MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def isResourceSufficient(orderIngredients):
    """Return True when oder can be made, False"""
    for item in orderIngredients:
        if orderIngredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_Coins():
    """Return the total calculated from coins inserted."""
    print("Please insert coins")
    total = int(input("How many quarters? :"))*0.25
    total += int(input("How many Dimes? :"))*0.1
    total += int(input("How many Nickles? :"))*0.05
    total += int(input("How many pennies? :"))*0.01
    return  total

def isTransactionSuccessful(moneyReceived, drinkCost):
    """Return True when the payment is accepted,
    or false if money is insufficient"""

    if moneyReceived >= drinkCost:
        global profit
        change = round(moneyReceived - drinkCost, 2)
        print(f"here is ${change} in change.")
        profit += drinkCost
        return True
    else:
        print("Sorry that's not enough money. money refunded.")
        return False

def makeCoffee(drinkName, orderIngredients):
    """Deduct the required ingredient from the resources."""
    for item in orderIngredients:
        resources[item] -= orderIngredients[item]
    print(f"here is your {drinkName} 🍵")

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino)")
    if choice == "off":
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money:{profit}")
    else:
        drink = MENU[choice]
        if isResourceSufficient(drink['ingredients']):
            payment = process_Coins()
            if isTransactionSuccessful(payment, drink['cost']):
                makeCoffee(choice, drink['ingredients'])
        # print(drink)
