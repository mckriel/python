import menu
import resources


def initialise_coffee_machine():
    global machine_resources
    global menu
    global cash_on_hand

    machine_resources = resources.resources
    menu = menu.MENU
    cash_on_hand = 0


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


def main():

    initialise_coffee_machine()
    continue_operations = True

    while continue_operations:
        user_choice = input('What would you like? (espresso/latte/cappuccino): ')

        if user_choice == 'off':
            break
        elif user_choice == 'report':
            resources_report(current_resources=machine_resources)
        else:
            drink = menu[user_choice]
            if check_resources_for_drink(drink_resources=drink['ingredients']):
                if process_coins(drink_cost=drink['cost']):
                    print('sweet')


main()
