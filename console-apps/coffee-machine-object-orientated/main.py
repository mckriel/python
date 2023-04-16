from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()[:-1]
    customer_choice = input(f'What drink would you like? {options}: ')

    if customer_choice == 'off':
        is_on = False
    elif customer_choice == 'report':
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(customer_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


# coffee_maker.is_resource_sufficient(menu.find_drink(customer_choice))
