from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneyMachine = MoneyMachine()
coffeeMaker = CoffeeMaker()
menu = Menu()
isOn = True

coffeeMaker.report()
moneyMachine.report()

while isOn:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):")
    if choice == "off":
        isOn = False
    elif choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        # print(coffeeMaker.is_resource_sufficient(drink))
        # if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
        is_enough_ingredients = coffeeMaker.is_resource_sufficient(drink)
        is_payment_successful = moneyMachine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
           coffeeMaker.make_coffee(drink)