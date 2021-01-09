from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    userInput = input(f"What would you like? ({coffee_menu.get_items()}):")

    if userInput == 'report':
        coffee_maker.report()
        money_machine.report()
        continue

    if userInput == 'off':
        break

    drink_choice = coffee_menu.find_drink(userInput)

    if coffee_maker.is_resource_sufficient(drink_choice):
        if money_machine.make_payment(drink_choice.cost):
            coffee_maker.make_coffee(drink_choice)
