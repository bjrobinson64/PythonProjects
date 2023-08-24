from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

isOn = True

coffeeMaker = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()

while isOn:
    choice = input(f"What would you like?({menu.get_items()}):")
    if choice == 'off':
        isOn = False
    elif choice == 'report':
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink):
            if moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)