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
        coffeeMaker.is_resource_sufficient(drink)