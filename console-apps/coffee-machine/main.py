import drinksmenu
import resources


def initialise_coffee_machine():
    global machine_resources
    global menu
    global cash_on_hand

    machine_resources = resources.resources
    menu = drinksmenu.MENU
    cash_on_hand = 0


def restock_machine():
    global machine_resources
    global cash_on_hand

    machine_resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    print('Machine has been restocked.')
    print(f'Current balance: ${cash_on_hand}')


def resources_report(current_resources):
    for x, y in current_resources.items():
        print(f'{x.capitalize()}: {y}')
    print(f'Cash on hand: ${cash_on_hand}')


def check_resources_for_drink(drink_resources):
    for item in drink_resources:
        if drink_resources[item] > machine_resources[item]:
            print(f'Not enough {item.capitalize()} to complete order.')
            return False
    return True


def update_cash_on_hand(cash_paid):
    global cash_on_hand
    cash_on_hand += cash_paid


def process_coins(drink_cost):
    total = int(input('How many Quarters?: ')) * 0.25
    total += int(input('How many Dimes?: ')) * 0.10

    if total > drink_cost:
        change = round(total - drink_cost, 2)
        print(f'You will be refunded: ${change:.2f}')

    if total >= drink_cost:
        update_cash_on_hand(cash_paid=total)
        return True
    print(f'The drink costs ${drink_cost}, however the total value of coins inserted was ${total}. Please try again.')
    return False


def consume_ingredients(drink_ingredients):
    for item in drink_ingredients:
        global machine_resources
        machine_resources[item] -= drink_ingredients[item]


def main():

    initialise_coffee_machine()
    continue_operations = True

    while continue_operations:
        user_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()

        if user_choice == 'off':
            break
        elif user_choice == 'report':
            resources_report(current_resources=machine_resources)
        elif user_choice == 'restock':
            restock_machine()
        else:
            drink = menu[user_choice]
            if check_resources_for_drink(drink_resources=drink['ingredients']):
                if process_coins(drink_cost=drink['cost']):
                    consume_ingredients(drink_ingredients=drink['ingredients'])
                    print(f'Here is your {user_choice.capitalize()}. Enjoy')


main()
